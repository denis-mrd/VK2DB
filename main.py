# -*- coding: utf8 -*-
__author__ = 'mrD'

import vk, VKtoken, time
session = vk.Session(access_token=VKtoken.access_token)
#session = vk.AuthSession(app_id='', user_login='', user_password='')
api = vk.API(session, v='5.74', lang='ru', timeout=10)

#connection = pypyodbc.connect(u'DRIVER={SQL Server Native Client 11.0};SERVER=(LocalDB)\\v11.0;Database=VK;Trusted_Connection=Yes;')
#cursor = connection.cursor()
user = api.users.get(user_id=52486985)
print(user)

