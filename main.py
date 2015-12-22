# -*- coding: utf8 -*-
__author__ = 'mrD'


import vk, pypyodbc, time
session = vk.Session(access_token='c901efb5f69c8d0ff58d0ea86c5139bf2596435b31640cb6e9b2598192ebbddc1e0c864f5aed834f9480d')
#session = vk.AuthSession(app_id='', user_login='', user_password='')
api = vk.API(session, v='5.37', lang='ru', timeout=10)

connection = pypyodbc.connect(u'DRIVER={SQL Server Native Client 11.0};SERVER=(LocalDB)\\v11.0;Database=VK;Trusted_Connection=Yes;')
cursor = connection.cursor()
user = api.users.get(user_id=8894167)
print(user)
