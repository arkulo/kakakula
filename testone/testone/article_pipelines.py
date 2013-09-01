#########################################################################
# File Name: article_pipelines.py
# Author: arkulo
# mail: arkulo@163.com
#########################################################################
#!/usr/bin/python
import json
import MySQLdb as mdb
import time
import hashlib

class TestonePipeline(object):
    def process_item(self, item, spider):
        conn = mdb.connect(host="localhost",user="root",passwd="",db="mydb",port=3307)
        with conn:
            try:
                hde = conn.cursor()
                cuTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
                title = mdb.escape_string(item['title'][0].encode('utf8'))
                content = mdb.escape_string(item['content'][0].encode('utf8'))
                native_sort = mdb.escape_string(item['native_sort'].encode('utf8'))

                sqlOne = "INSERT INTO a_article VALUES(null,'%s','','%s','%s','%s','%s','%s','%s','%s')" %(title,item['source'],cuTime,content,item['section'],item['keyword'],item['link'],native_sort)
                hde.execute("set names utf8")
                hde.execute(sqlOne)

                lastId = hde.lastrowid#hde.execute("select LAST_INSERT ID()")
                #for path in item['image_urls']:
                if(""!=item['image_paths']):
                    sqlTwo = "INSERT INTO a_article_image VALUES(null,%d,'%s','%s')" %(lastId,item['image_paths'],item['image_urls'])
                    hde.execute(sqlTwo)
                
                #store crawl url histroy in mysql table
                tmp = hashlib.md5(item['link'])
                link = tmp.hexdigest()
                site = "yaolan"
                sqlThree = "INSERT INTO crawl_history VALUES(null,'%s','%s','%s')" %(item['link'],link,site)
                hde.execute(sqlThree)
            except mdb.Error,e:
                print "Error %d: %s" %(e.args[0],e.args[1])
        return item   
