import scrapy


class DangSpider(scrapy.Spider):
    name = "dang"
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["https://category.dangdang.com/cp01.54.06.19.00.00.html"]

    def parse(self, response):
        print('=======================')
