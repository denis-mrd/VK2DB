# -*- coding: utf8 -*-
__author__ = 'mrD'

import vk
import VKtoken #отсюда берем токен приложения из-под которого работаем: https://vk.com/dev/first_guide
import postgresql
import time

print('Started at', time.ctime())
session = vk.Session(access_token=VKtoken.access_token)
api = vk.API(session, v='5.74', lang='ru', timeout=10)
db = postgresql.open('pq://postgres:postgres@localhost:5432/vk')

def friends2db (userid):
    info = ['id', 'domain', 'nickname', 'screen_name', 'first_name', 'last_name', 'maiden_name', 'sex', 'bdate', 'city', 'home_town', 'country', 'photo_max_orig', 'exports', 'site', 'deactivated', 'hidden', 'occupation', 'status', 'activities', 'interests', 'music', 'movies', 'tv', 'books', 'games', 'quotes', 'about']
    fields = ', '.join(info)
    friends = api.friends.get(user_id=userid)
    vkuser = api.users.get(user_ids=userid, fields=fields)
    friends_all = friends['count']
    friends_counter = 0
    print('Пользователь %s %s имеет %s друзей' % (vkuser[0]['first_name'], vkuser[0]['last_name'], friends_all))
    try:
        columns = ''.join([item + ' character varying, ' for item in info])[:-2]
        create_query = 'CREATE TABLE public.friends_' + str(userid) + ' (' + columns + ')'
        db.query(create_query)
    except postgresql.exceptions.DuplicateTableError as err:
        print('DuplicateTableError for user:', userid)
        db.query('DROP TABLE public.friends_' + str(userid)) #почему-то не работает

    for x in friends['items']: #для каждого ИДшника из списка друзей
        try:
            user = api.users.get(user_ids=x, fields=fields)
            friends_counter += 1
            print('Обрабатывается: ', str(user[0]['first_name']), str(user[0]['last_name']), str(friends_counter) + '/' + str(friends_all))

        except UnicodeEncodeError as err:
            print('UnicodeEncodeError on user:', user[0]['id'])
            print(err)
            pass

        ins_id = "INSERT INTO public.friends_" + str(userid) + "(id) VALUES ('" + str(user[0]['id']) + "');"
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

                upd_val = "UPDATE public.friends_" + str(userid) + " SET " + str(key) + " = '" + str(val) + "' where id = '" + str(user[0]['id']) + "';"
                db.query(upd_val)

            except postgresql.exceptions.UndefinedColumnError as err:
                print('UndefinedColumnErroron on user:', user[0]['id'])
                print(err)
                pass
            except postgresql.exceptions.SyntaxError as err:
                print('SyntaxErroron on user:', user[0]['id'])
                print(err)
                pass
            except postgresql.exceptions.UndefinedFunctionError as err:
                print('UndefinedFunctionError on user:', user[0]['id'])
                print(err)

        time.sleep(1)

    print('Все друзья успешно загружены в базу данных!')

userid = int(input('Ведите id пользователя Вконтакте: '))
friends2db(userid)

print('Ended at', time.ctime())

#сделать лог-файл

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