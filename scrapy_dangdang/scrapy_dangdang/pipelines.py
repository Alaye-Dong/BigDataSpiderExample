# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface


# 导入MongoDB的Python驱动
from pymongo import MongoClient

class ScrapyDangdangPipeline:
    def __init__(self):
        # 连接到MongoDB服务器
        self.client = MongoClient('localhost', 27017)
        # 选择数据库
        self.db = self.client['dangdang']
        # 选择集合
        self.collection = self.db['books']

    def open_spider(self, spider):
        # 可以在这里进行一些初始化操作
        pass

    def process_item(self, item, spider):
        # 将爬取到的item（书籍信息）插入到MongoDB集合中
        self.collection.insert_one(dict(item))
        # 继续传递item给下一个Pipeline处理
        return item

    def close_spider(self, spider):
        # 关闭MongoDB连接
        self.client.close()


# 导入urllib库中的request模块，用于发送网络请求
import urllib.request
class DangdangDownloadPipeline:
    def process_item(self, item, spider):
        # 拼接书籍封面的URL
        url = 'http:' + item.get('src')
        # 拼接保存封面图片的文件路径和名称
        filename = './books/' + item.get('name') + '.jpg'

        # 发送网络请求，下载封面图片并保存到本地
        urllib.request.urlretrieve(url = url, filename = filename)

        # 继续传递item给下一个Pipeline处理
        return item

