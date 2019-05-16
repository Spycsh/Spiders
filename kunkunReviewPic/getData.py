import re
import requests
from bs4 import BeautifulSoup as BS
import csv

def open_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.103 Safari/537.36'}
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    html = response.text
    return html

def get_danmu_id(html):   # Ctrl+U查看网页源码，然后Ctrl+F搜索cid
    try:
        soup = BS(html, 'lxml')
        danmu_id = re.findall(r'cid=(\d+)&', html)[0]  # 一个视频只有一个弹幕号
        print(danmu_id)
        # print(title, author)
        return danmu_id
    except:
        print('视频不见了哟')
        return False

def csv_write(tablelist):
    # tableheader = ['出现时间', '弹幕模式', '字号', '颜色', '发送时间' ,'弹幕池', '发送者id', 'rowID', '弹幕内容']
    with open('danmu.csv', 'w', newline='', errors='ignore') as f:
        writer = csv.writer(f)
        writer.writerow(tablelist)
        for row in tablelist:
            writer.writerow(row)