import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud


def main():
    text = open(r'children.txt', 'r', encoding='utf-8').read()
    print(text)
    wc = WordCloud(font_path=r"1.ttf", width=400,
                   height=400, max_font_size=50,
                   max_words=300, background_color='pink', colormap='Accent')
    wc.generate(text)
    wc.to_file(r"result_shengri.png")

    plt.figure("Happy Birthday")
    plt.imshow(wc)
    plt.axis("off")

    import matplotlib.font_manager
    font = matplotlib.font_manager.FontProperties(fname='1.ttf')
    plt.title('母上生日愉快！', loc='left', fontproperties=font,
              fontsize='large')
    plt.title('2019/5/19', loc='right', fontproperties=font,
              fontsize='large')
    # plt.title('Let me say Happy birthday to you in different languages, my grandmother!', fontproperties=font,fontsize='large',fontweight = None)
    # plt.title('Let me say Happy birthday to you in different languages, my colleague!', bbox=dict( facecolor='orange',edgecolor='orange', alpha=0.65))

    plt.show()

if __name__ == "__main__":
    main()