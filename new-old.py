# -*- coding: utf8 -*-
__author__ = 'mrD'


import vk, pypyodbc
session = vk.Session(access_token='c901efb5f69c8d0ff58d0ea86c5139bf2596435b31640cb6e9b2598192ebbddc1e0c864f5aed834f9480d')
#session = vk.AuthSession(app_id='5129430 ', user_login='89667613408', user_password='boat123')
api = vk.API(session, v='5.37', lang='ru', timeout=10)

connection = pypyodbc.connect(u'DRIVER={SQL Server Native Client 11.0};SERVER=(LocalDB)\\v11.0;Database=VK;Trusted_Connection=Yes;')
cursor = connection.cursor()

#реализуем ввод значиений через функцию
def update (column = None, value = None, id = None):
    if value is '':
        print()
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
        print('ProgrammingError: ', err)

    except pypyodbc.DataError as err:
        print('DataError: ', err)

    except pypyodbc.IntegrityError as err:
        print('IntegrityError: ', err)

    except TypeError as err:
        print('TypeError: ', err)

    except UnicodeEncodeError as err:
        print('UnicodeEncodeError: ', err)

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



id = int(input('Ведите id пользователя ВКонтакте: '))

user2db(id)
friends2db(id)



cursor.close()
connection.close()
print('done')

#залить код на гитхаб
#подумать по поводу формата даты