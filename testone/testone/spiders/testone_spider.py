#########################################################################
# File Name: testone_spider.py
# Author: arkulo
# mail: arkulo@163.com
#########################################################################
#!/usr/bin/python
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.utils.response import open_in_browser
from testone.items import TestoneItem

class ImageDownloaderSpider(BaseSpider):
    name = "testone"
    allowed_domains = ["yaolan.com"]
    start_urls = [
        "http://www.yaolan.com/parenting/201307031423271.shtml"        
    ]

#    def parse(self,response):
#        hxs = HtmlXPathSelector(response)
#        images = hxs.select("//div[@class='cont_font114']/p/img/@src").extract()
#        items = []
#        for image in images:
#            item = TestoneItem()
#            item['title'] = hxs.select("//h1/text()").extract()
#            item['link'] = response.url
#            item['content'] = hxs.select("//div[@class='cont_font114']").extract()
#            item['source'] = "yaolan.com"
#            item['section'] = 1
#            item['keyword'] = 1
#            item['image_urls'] = [image]
#            items.append(item)
#        return items
    def parse(self,response):
        print response.url
