__author__ = 'mrD'
# -*- coding: utf8 -*-

import vk, pypyodbc
session = vk.Session(access_token='c901efb5f69c8d0ff58d0ea86c5139bf2596435b31640cb6e9b2598192ebbddc1e0c864f5aed834f9480d')
#session = vk.AuthSession(app_id='5129430 ', user_login='89667613408', user_password='boat123')
api = vk.API(session, v='5.37', lang='ru', timeout=10)
#api.method.name(param=value)
#print(api.users.get(user_ids=58786921))
#print (api.users.get(user_id = 8894167, fields = 'sex, bdate, city, country, photo_max_orig, contacts, connections, site'))
connection = pypyodbc.connect(u'DRIVER={SQL Server Native Client 11.0};SERVER=(LocalDB)\\v11.0;Database=VK;Trusted_Connection=Yes;')
cursor = connection.cursor()
id = 8894167
vkuser = api.users.get(user_ids=id, fields='sex, bdate, city, country, photo_50, photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig, photo_id, online, online_mobile, domain, has_mobile, contacts, connections, site, education, universities, schools, can_post, can_see_all_posts, can_see_audio, can_write_private_message, status, last_seen, common_count, relation, relatives, counters, screen_name, maiden_name, timezone, occupation,activities, interests, music, movies, tv, books, games, about, quotes, personal, friend_status, military, career')
for key in vkuser[0].keys():
    d = vkuser[0]
    column = key
    id = vkuser[0]['id']
    s = 'update friends set {} = (?) where id = {}'
    insert = ('' + s + '').format(column, id)
    value = []
    value.append(d[key])
    print (insert)
    print (value)
    try:
        cursor.execute(insert, value)
        cursor.commit()
#    except ProgrammingError:
#       print (ProgrammingError)

# cursor.close()
# connection.close()
print('done')
