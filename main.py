# -*- coding: utf8 -*-
__author__ = 'mrD'

import vk
import VKtoken
import postgresql
import time
session = vk.Session(access_token=VKtoken.access_token)
api = vk.API(session, v='5.74', lang='ru', timeout=10)
db = postgresql.open('pq://postgres:postgres@localhost:5432/vk')

userid = int(input('Ведите id пользователя Вконтакте: '))
fields = 'id, domain, nickname, screen_name, first_name, last_name, maiden_name, sex, bdate, city, home_town, country, contacts, photo_max_orig, connections, exports, site, deactivated, hidden, occupation, relation, status, activities, interests, music, movies, tv, books, games, quotes, about'
friends = api.friends.get(user_id=userid)
vkuser = api.users.get(user_ids=userid, fields=fields)
friends_all = friends['count']
friends_counter = 0
print('Пользователь %s %s имеет %s друзей' % (vkuser[0]['first_name'], vkuser[0]['last_name'], friends_all))

for x in friends['items']: #для каждого ИДшника из списка друзей
    user = api.users.get(user_ids=x, fields=fields)
    friends_counter += 1
    print('Обрабатывается: ', user[0]['first_name'], user[0]['last_name'], str(friends_counter) + '/' + str(friends_all))
    ins_id = "INSERT INTO public.friends (id) VALUES ('" + str(user[0]['id']) + "');"
    db.query(ins_id)

    for key in user[0]: #создаем запрос
        val = str(user[0][key]).replace("'", "")
        try:
            if key == 'city':
                val = str(user[0][key]['title'])
            elif key == 'country':
                val = str(user[0][key]['title'])
            elif key == 'occupation':
                val = str(user[0][key]['name'])
            elif key == 'relation_partner':
                val = str(user[0][key]['first_name']) + ' ' + str(user[0][key]['last_name'])

            upd_val = "UPDATE public.friends SET " + str(key) + " = '" + val + "' where id = " + str(user[0]['id'])
            db.query(upd_val)

        except postgresql.exceptions.UndefinedColumnError as err:
            print('UndefinedColumnError')
        except postgresql.exceptions.SyntaxError as err:
            print('SyntaxError')
    time.sleep(1)

print('Все друзья успешно загружены в базу данных!')

#обернуть все это в функцию
#подумать по поводу формата даты

"""
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


"""