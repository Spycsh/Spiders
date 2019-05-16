import matplotlib.pyplot as plt  # 数学绘图库
import jieba  # 分词库
from wordcloud import WordCloud  # 词云库
from PIL import Image
import numpy as np
import csv
from bs4 import BeautifulSoup as BS
from getData import open_url, get_danmu_id, csv_write

from Mongo_link import insertToDatabase, findByColor

def get_danmulist_by_aid( video_id ):
    video_url ='http://www.bilibili.com/video/{}/'.format(video_id)
    video_html = open_url(video_url)
    # 获得danmuid
    danmu_id = get_danmu_id(video_html)
    if danmu_id:
        danmu_url = 'http://comment.bilibili.com/{}.xml'.format(danmu_id)
        danmu_html = open_url(url=danmu_url)
        soup = BS(danmu_html, 'lxml')
        all_d = soup.select('d')
        danmu_list = []
        for d in all_d:
            danmu_list.append(d.get_text())
        print(danmu_list)
        csv_write(danmu_list)

# 弹幕出现的时间，以秒为单位
# 弹幕的模式：1～3 滚动弹幕 4 底端弹幕 5 顶端弹幕 6 逆向弹幕 7 精准定位 8 高级弹幕
# 字号：12 非常小 16 特小 18 小 25 中 36 大 45 很大 64 特别大
# 字体的颜色：将 HTML 六位十六进制颜色转为十进制表示，例如 #FFFFFF 会被存储为 16777215，因为 (FFFFFF)16=(16777215)10
# Unix 时间戳，以毫秒为单位，基准时间为 1970-1-1 08:00:00
# 弹幕池：0 普通池 1 字幕池 2 特殊池（注：目前特殊池为高级弹幕专用）
# 发送者的 ID，用于『屏蔽此弹幕的发送者』功能
# 弹幕在弹幕数据库中 rowID，用于『历史弹幕』功能
        import time
        all_danmu_info = []
        for d in all_d:
            one_danmu_info = d['p'].split(',')
            all_danmu_info.append({
                "弹幕内容": d.get_text(),
                "出现的时间": one_danmu_info[0],
                "弹幕的模式": one_danmu_info[1],
                "字号": one_danmu_info[2],
                "字体颜色": one_danmu_info[3],
                "Unix时间戳": time.localtime(int(one_danmu_info[4])),
                "弹幕池": one_danmu_info[5],
                "发送者ID": one_danmu_info[6],
            })

        # 保存所有弹幕信息到数据库
        insertToDatabase(all_danmu_info)
        # 找到橙色弹幕对应的弹幕
        findByColor('15138834')

def main():
    all_danmu_info = get_danmulist_by_aid('av49868991')
    # 1、读入txt文本数据
    text = open(r'danmu.csv').read()

    cut_text = jieba.cut(text)
    result = "/".join(cut_text)
    # print(result)

    image = Image.open(r'caixukun_ok.png')
    graph = np.array(image)

    wc = WordCloud(font_path=r"851CHIKARA-DZUYOKU-kanaB-2.ttf", background_color='white', width=1600,
                   height=1200, max_font_size=50,
                   max_words=2000, mask=graph, colormap='Accent')  # ,min_font_size=10)#,mode='RGBA',colormap='pink')
    wc.generate(result)
    wc.to_file(r"result.png")  # 按照设置的像素宽高度保存绘制好的词云图，比下面程序显示更清晰

    # 4、显示图片
    plt.figure("蔡徐坤_弹幕图")  # 指定所绘图名称
    plt.imshow(wc)  # 以图片的形式显示词云
    plt.axis("off")  # 关闭图像坐标系
    plt.show()

if __name__ == "__main__":
    main()