import pymongo
import os
import re
from datetime import datetime, timedelta


class DBHandler:
    def __init__(self):
        self.file_folder_path = "outlook_emails"
        self.DB_name = "Outlook"
        self.DB_site = "inbox"
        self.mycol = self.connect_to_DB()

    def connect_to_DB(self):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient[self.DB_name]
        mycol = mydb[self.DB_site]
        return mycol

    def store_to_DB(self, subject, sender, datetime_received):
        subject = str(subject)
        rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
        new_title = re.sub(rstr, "_", subject)  # 替换为下划线
        item = dict({"subject": subject, "sender_name": sender.name, "sender_email": sender.email_address,
                     "datetime_received": datetime_received + timedelta(hours=2),
                     "file_path": os.path.join(self.file_folder_path, new_title + ".html")})
        self.mycol.insert(item)
        # f = open(subject+'.html', 'w')
        # f.write()

    def store_HTML(self, subject, body):
        subject = str(subject)
        rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
        new_title = re.sub(rstr, "_", subject)  # 替换为下划线
        f = open(os.path.join(self.file_folder_path, new_title + ".html"), 'w', encoding='utf-8')
        f.write(body)
