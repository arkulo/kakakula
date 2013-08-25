#########################################################################
# File Name: yaolan_spider.py
# Author: arkulo
# mail: arkulo@163.com
#########################################################################
#!/usr/bin/python

#from scrapy.spider import BaseSpider
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from testone.items import TestoneItem

class ZebraSpider(CrawlSpider):
    name = "zebra"
    allowed_domains = ['yaolan.com']
    start_urls = ["http://www.yaolan.com/preconception/yqys/"]
    rules = (
#Rule(SgmlLinkExtractor(allow=('nutrition'))),
        Rule(SgmlLinkExtractor(allow=('\/nutrition\/')),callback='parse_item'),
    )

    def parse_item(self,response):
        self.log('page:%s' % response.url)
        hxs = HtmlXPathSelector(response)
        images = hxs.select("//div[@class='cont_font114']/p/img/@src").extract()
        items = []
        for image in images:
            item = TestoneItem()
            item['title'] = hxs.select("//h1/text()").extract()
            item['link'] = response.url
            item['content'] = hxs.select("//div[@class='cont_font114']").extract()
            item['source'] = "yaolan.com"
            item['section'] = 1
            item['keyword'] = 1
            item['image_urls'] = [image]
            items.append(item)
        return items

