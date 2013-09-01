# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

#class TestonePipeline(object):
#    def process_item(self, item, spider):
#        return item
#
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request

class ImageDownloaderPipeline(ImagesPipeline):

    def get_media_requests(self,item,info):
#        for image_url in item['image_urls']:
#            yield Request(image_url)
        if(""!=item['image_urls']):
            yield Request(item['image_urls'])

    def item_completed(self,results,item,info):
        image_paths = [x['path'] for ok,x in results if ok]
        if(image_paths):
            item['image_paths'] = image_paths[0]
        else:
            item['image_paths'] = ""
#print image_paths
        return item
