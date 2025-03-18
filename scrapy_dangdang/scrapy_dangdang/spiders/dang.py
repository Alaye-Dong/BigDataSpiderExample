import scrapy
from ..items import ScrapyDangdangItem

class DangSpider(scrapy.Spider):
    name = "dang"
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["https://category.dangdang.com/cp01.54.06.19.00.00.html"]

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


