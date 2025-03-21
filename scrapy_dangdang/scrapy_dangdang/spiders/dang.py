import scrapy
from scrapy import cmdline

from ..items import ScrapyDangdangItem
# cd scrapy_dangdang/scrapy_dangdang/spiders
# scrapy crawl dang
class DangSpider(scrapy.Spider):
    name = "dang"
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["https://category.dangdang.com/cp01.54.06.19.00.00.html"]

    base_url = 'https://category.dang.com/pg'
    page = 1
    MAX_PAGE = 3

    def parse(self, response):
        # 提示当前正在爬取的页面
        self.logger.info(f"正在爬取第 {self.page} 页")

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

            # 提示即将爬取下一页
            self.logger.info(f"准备爬取第 {self.page} 页")
            yield scrapy.Request(url = url, callback = self.parse)


if __name__ == '__main__':
    cmdline.execute("scrapy crawl dang".split())
