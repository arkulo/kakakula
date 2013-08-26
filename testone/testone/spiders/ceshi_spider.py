#########################################################################
# File Name: ceshi_spider.py
# Author: arkulo
# mail: arkulo@163.com
#########################################################################
#!/usr/bin/python
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from testone.items import TestoneItem
from scrapy.http import Request
import pdb
class CeshiSpider(BaseSpider):
    name = "ceshione"
    allowed_domains = ["yaolan.com"]
    start_urls = [
        "http://www.yaolan.com/sitemap/"
    ]

    def parse(self,response):
        hxs = HtmlXPathSelector(response)
        res = hxs.select("//div[@class='guidebox clear']/ul/li/a/@href").extract()
        for url in res:
            if(url.find("preconception/yqys")>0):
                yield Request(url,callback=lambda response:self.parse_list(response,1))

    def parse_list(self,response,category):
        hxs = HtmlXPathSelector(response)
        res = hxs.select("//div[@id='pmm_mid']//li/a/@href").extract()
        for url in res:
            url = "http://www.yaolan.com"+url
            yield Request(url,callback=lambda response:self.parse_item(response,category))

#        baseUrl = response.url
#        pages = hxs.select("//div[@class='cc_page']/a/@href").extract()
#        for page in pages:
#            pageUrl = baseUrl+page
#            yield Request(pageUrl,callback=lambda response:self.parse_list(response,category))
#
    def parse_item(self,response,category):
#        print response.url
#        self.log('page:%s' % response.url)
        hxs = HtmlXPathSelector(response)
        item = TestoneItem()
        item['title'] = hxs.select("//h1/text()").extract()
        item['link'] = response.url
        item['content'] = hxs.select("//div[@class='cont_font114']").extract()
        item['source'] = "yaolan.com"
        item['section'] = category
        item['keyword'] = 1
        item['image_urls'] = hxs.select("//div[@class='cont_font114']//img/@src").extract()[0] 
        item['native_sort'] = hxs.select("//div[@class='crumb clear']/a[3]/@title").extract()[0]
        return item

