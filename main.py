# -*- coding: utf8 -*-
__author__ = 'mrD'

import vk, VKtoken, postgresql,  time
session = vk.Session(access_token=VKtoken.access_token)
api = vk.API(session, v='5.74', lang='ru', timeout=10)
db = postgresql.open('pq://postgres:postgres@localhost:5432/vk')
ins = db.prepare("INSERT INTO users (userid, name, surname) VALUES ($1, $2, $3)")

userid = 52486985
user = api.users.get(user_id = userid)
friends = api.friends.get(user_id = userid)
vkuser = api.users.get(user_ids = userid, fields = 'photo_id, deactivated, verified, sex, bdate, city, country, home_town, has_photo, photo_max_orig, online, online_mobile, domain, has_mobile, contacts, site, education, universities, schools, status, last_seen, followers_count, common_count, occupation, nickname, relatives, relation, personal, connections, exports, wall_comments, activities, interests, music, movies, tv, books, games, about, quotes, can_post, can_see_all_posts, can_see_audio, can_write_private_message, can_send_friend_request, is_favorite, is_hidden_from_feed, hidden, timezone, screen_name, maiden_name, is_friend, friend_status, career, military, blacklisted, blacklisted_by_me, counters')

print('user %1 ', user[0]['first_name'], user[0]['last_name'], friends['count'])


#ins(userid, "afiskon", "123")