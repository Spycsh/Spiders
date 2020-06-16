#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
from DBHandler import DBHandler

from exchangelib import DELEGATE, Account, Credentials

print("Please enter email address")
email_address = input()
print("Please enter username:\n")
username = input()
print("Please enter password:\n")
password = input()
print('waiting...\n')

credentials = Credentials(
    username=username,  # Or myusername@example.com for O365
    password=password
)
account = Account(
    primary_smtp_address=email_address,
    credentials=credentials,
    autodiscover=True,
    access_type=DELEGATE
)

dbHandler = DBHandler()

# Print first 100 inbox messages in reverse order
# 收件箱 inbox
for item in account.inbox.all().order_by('-datetime_received')[0:]:
    # print(item.subject, item.body, item.attachments)
    dbHandler.connect_to_DB()
    try:
        dbHandler.store_to_DB(item.subject, item.sender, item.datetime_received)
        dbHandler.store_HTML(item.subject, item.body)
    except AttributeError:
        print("'NoneType' object")
