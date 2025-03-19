# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface


class ScrapyDangdangPipeline:
    # 当Spider开启时执行初始化方法
    def open_spider(self, spider):
        # 打开或创建一个名为book.json的文件，用于存储爬取的数据
        self.fp = open("book.json", "w", encoding="utf-8")

    # item: yield的book对象
    def process_item(self, item, spider):
        # 将爬取到的item（书籍信息）转换为字符串形式并写入文件
        self.fp.write(str(item))

        # 继续传递item给下一个Pipeline处理
        return item

    def close_spider(self, spider):
        # 当Spider关闭时，关闭文件写入流
        self.fp.close()

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

