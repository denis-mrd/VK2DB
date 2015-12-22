# -*- coding: utf8 -*-
__author__ = 'mrD'


import vk, pypyodbc, time
session = vk.Session(access_token='')
#session = vk.AuthSession(app_id='', user_login='', user_password='')
api = vk.API(session, v='5.37', lang='ru', timeout=10)

connection = pypyodbc.connect(u'DRIVER={SQL Server Native Client 11.0};SERVER=(LocalDB)\\v11.0;Database=VK;Trusted_Connection=Yes;')
cursor = connection.cursor()

#реализуем ввод значиений через функцию
def update (column = None, value = None, id = None):
    if value is '':
        None
    try:
        if "'" in value:
            value.replace("'", '"')
    except TypeError as err:
        None

    #сделать разворачивание листов в словари
    # if type(value) is list:
    #     try:
    #         value = value[0]
    #     except IndexError as err:
    #         print (err)
    if type(value) is dict:
        d = value
        for key in d:
            newcolumn = ''
            newcolumn = column + '_' + key
            value = d.get(key)

            update(newcolumn, value, id)

    query = "UPDATE friends SET {} = '{}' WHERE id = {}".format(column, value, id)

    try:
        cursor.execute(query)
        cursor.commit()

    except pypyodbc.ProgrammingError as err:
        None

    except pypyodbc.DataError as err:
        None

    except pypyodbc.IntegrityError as err:
        None

    except TypeError as err:
        None

    except UnicodeEncodeError as err:
        None


#внесение информации о пользователе в БД по ИД
def user2db (id):
    insert = "INSERT INTO friends (id) VALUES ('{}')".format(id)
    cursor.execute(insert)
    cursor.commit()
    vkuser = api.users.get(user_ids = id, fields = 'sex, bdate, city, country, photo_50, photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig, photo_id, online, online_mobile, domain, has_mobile, contacts, connections, site, education, universities, schools, can_post, can_see_all_posts, can_see_audio, can_write_private_message, status, last_seen, common_count, relation, relatives, counters, screen_name, maiden_name, timezone, occupation,activities, interests, music, movies, tv, books, games, about, quotes, personal, friend_status, military, career')
    for key in vkuser[0].keys():
        column = key
        id = vkuser[0]['id']
        value = vkuser[0][key]
        update(column, value, id)

#получение списка друзей и занесение каждого из них в БД
def friends2db (id):
    friends = api.friends.get(user_id = id)
    for x in friends['items']:
        user2db(x)

#citizens = api.users.search(count=1000, country=1, city=18058)
members = api.groups.getMembers(group_id='63480208', offset='0')
print('Участников в группе ', members['count'])
counter = 0

for x in members['items']:
    member = api.users.get(user_ids =x, fields='sex')

    if member[0]['sex'] == 1:
        user2db(int(x))
        counter += 1
        print(counter, 'телки в базе')
        time.sleep(1)

#print('Жителей найдено ', citizens['count'])
# for x in citizens['items']:
#     ids = int(x['id'])
#     user2db(ids)


# id = int(input('Ведите id пользователя ВКонтакте: '))
#
# user2db(id)
# friends2db(id)



cursor.close()
connection.close()
print('done')

#подумать по поводу формата даты