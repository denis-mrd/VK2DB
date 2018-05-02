# -*- coding: utf8 -*-
__author__ = 'mrD'

import vk, VKtoken, postgresql, time
session = vk.Session(access_token=VKtoken.access_token)
api = vk.API(session, v='5.74', lang='ru', timeout=10)
db = postgresql.open('pq://postgres:postgres@localhost:5432/vk')

userid = int(input('Ведите id пользователя Вконтакте: '))
info = 'id, domain, nickname, screen_name, first_name, last_name, maiden_name, sex, bdate'#, city, home_town, country, contacts, photo_max_orig, connections, exports, site, last_seen, deactivated, hidden, career, education, military, occupation, relatives, relation, schools, status, personal, activities, interests, music, movies, tv, books, games, quotes, about'
friends = api.friends.get(user_id=userid)
vkuser = api.users.get(user_ids=userid, fields=info)
friends_all = friends['count']
friends_counter = 0
print('Пользователь %s %s имеет %s друзей' % (vkuser[0]['first_name'], vkuser[0]['last_name'], friends_all))

for x in friends['items']: #для каждого ИДшника из списка друзей
    user = api.users.get(user_ids=x, fields=info)
    friends_counter += 1
    print('Обрабатывается: ', user[0]['first_name'], user[0]['last_name'], str(friends_counter) + '/' + str(friends_all))
    ins_id = "INSERT INTO public.friends (id) VALUES ('" + str(user[0]['id']) + "');"
    db.query(ins_id)

    for key in user[0]: #создаем запрос
        upd_val = "UPDATE public.friends SET " + str(key) + " = '" + str(user[0][key]) + "' where id = " + str(user[0]['id'])
        db.query(upd_val)

    time.sleep(1)

print('Все друзья успешно загружены в базу данных!')