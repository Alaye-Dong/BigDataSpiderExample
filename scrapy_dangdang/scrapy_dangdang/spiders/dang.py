import scrapy
from ..items import ScrapyDangdangItem

class DangSpider(scrapy.Spider):
    name = "dang"
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["https://category.dangdang.com/cp01.54.06.19.00.00.html"]

    base_url = 'https://category.dang.com/pg'
    page = 1
    MAX_PAGE = 3

    def parse(self, response):
        li_list = response.xpath('//ul[@id="component_59"]/li')

        for li in li_list:
            src = li.xpath('.//img/@data-original').extract_first()
            # 处理第一张非懒加载的图片
            if not src:
                src = li.xpath('.//img/@src').extract_first()

            name = li.xpath('.//img/@alt').extract_first()
            price = li.xpath('.//p[@class="price"]/span[1]/text()').extract_first()

            book = ScrapyDangdangItem(src = src, name = name, price = price)

            # 返回一个值给管道
            yield book

        # 翻页
        if self.page < self.MAX_PAGE:
            self.page += 1
            url = self.base_url + str(self.page) + '-cp01.54.06.19.00.00.html'

            yield scrapy.Request(url = url, callback = self.parse)
