import pymongo
# 定义一些和数据库的操作

def insertToDatabase(all_danmu_info):
    client = pymongo.MongoClient(host='localhost', port=27017)

    db = client['bilibili']

    collection = db['danmu']

    result = collection.insert_many(all_danmu_info)
    # print(result)


def findByColor(decimal_num):
    client = pymongo.MongoClient(host='localhost', port=27017)

    db = client['bilibili']

    collection = db['danmu']

    results = collection.find({"字体颜色": decimal_num})
    for result in results:
        print(result)
