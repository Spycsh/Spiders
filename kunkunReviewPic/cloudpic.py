import matplotlib.pyplot as plt  # 数学绘图库
import jieba  # 分词库
from wordcloud import WordCloud  # 词云库
from PIL import Image
import numpy as np
import csv
from bs4 import BeautifulSoup as BS
from getData import open_url, get_danmu_id, csv_write


def get_danmulist_by_aid( video_id ):
    video_url ='http://www.bilibili.com/video/{}/'.format(video_id)
    video_html = open_url(video_url)
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

def main():
    get_danmulist_by_aid('av49868991')
    # 1、读入txt文本数据
    # text = open(r'C:\Users\Spycsh\Downloads\xiaoao.txt', "r").read()
    text = open(r'danmu.csv').read()

    cut_text = jieba.cut(text)
    result = "/".join(cut_text)
    # print(result)

    image = Image.open(r'caixukun_ok.png')
    graph = np.array(image)

    wc = WordCloud(font_path=r"851CHIKARA-DZUYOKU-kanaB-2.ttf", background_color='white', width=1600,
                   height=1200, max_font_size=50,
                   max_words=2000, mask=graph, colormap= 'Accent')  # ,min_font_size=10)#,mode='RGBA',colormap='pink')
    wc.generate(result)
    wc.to_file(r"result.png")  # 按照设置的像素宽高度保存绘制好的词云图，比下面程序显示更清晰

    # 4、显示图片
    plt.figure("蔡徐坤_弹幕图")  # 指定所绘图名称
    plt.imshow(wc)  # 以图片的形式显示词云
    plt.axis("off")  # 关闭图像坐标系
    plt.show()

if __name__ == "__main__":
    main()