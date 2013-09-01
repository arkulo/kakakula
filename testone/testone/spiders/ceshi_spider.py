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
import MySQLdb as mdb
import hashlib

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
            if(url.find("preconception/fqsh")>0):
                yield Request(url,callback=lambda response:self.parse_list(response,1))

    def parse_list(self,response,category):
        #mysql instance
        print "["+response.url+"]"
        conn = mdb.connect(host="localhost",user="root",passwd="",db="mydb",port=3307)
        with conn:
            try:
                hxs = HtmlXPathSelector(response)
                res = hxs.select("//div[@id='pmm_mid']//li/a/@href").extract()
                for url in res:
                    url = "http://www.yaolan.com"+url
                    hde = conn.cursor()
                    tmp1 = hashlib.md5(url)
                    md5url = tmp1.hexdigest()
                    sqlOne = "SELECT COUNT(*) FROM crawl_history WHERE url_md5='%s'" %md5url
                    hd = hde.execute(sqlOne)
                    result = hde.fetchone()
                    #print result
                    if(result[0]<1):
                        yield Request(url,callback=lambda response:self.parse_item(response,category))

                subart = hxs.select("//ul[@class='time_list']//a/@href").extract()
                for suburl in subart:
                    suburl = "http://www.yaolan.com"+suburl
                    tmp3 = hashlib.md5(suburl)
                    submd5url = tmp3.hexdigest()
                    sqlThree = "SELECT COUNT(*) FROM crawl_history WHERE url_md5='%s'" %submd5url
                    hd3 = hde.execute(sqlThree)
                    result3 = hde.fetchone()
                    #print result
                    if(result3[0]<1):
                        yield Request(suburl,callback=lambda response:self.parse_item(response,category))
                        print suburl                        


                baseUrl = "http://www.yaolan.com/preconception/fqsh/"#response.url
                pages = hxs.select("//div[@class='cc_page']/a/@href").extract()
                for page in pages:
                    pageUrl = baseUrl+page
                    tmp2 = hashlib.md5(pageUrl)
                    md5_url = tmp2.hexdigest()
                    sqlTwo = "SELECT COUNT(*) FROM crawl_history WHERE url_md5='%s'" %md5_url
                    hd1 = hde.execute(sqlTwo)
                    result1 = hde.fetchone()
                    if(result1[0]<1):
                        yield Request(pageUrl,callback=lambda response:self.parse_list(response,category))
                        sqlFour = "INSERT INTO crawl_history VALUES(null,'%s','%s','%s')" %(pageUrl,md5_url,'yaolan')
                        hde.execute(sqlFour)
            except mdb.Error,e:
                print "Error %d: %s" %(e.args[0],e.args[1])

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
        tmp_img = hxs.select("//div[@class='cont_font114']//img/@src").extract()
        if tmp_img:
            item['image_urls'] = tmp_img[0]
        else:
            item['image_urls'] = ""
        item['native_sort'] = hxs.select("//div[@class='crumb clear']/a[3]/@title").extract()[0]
        return item

