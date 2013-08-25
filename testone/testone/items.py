# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class TestoneItem(Item):
    title = Field()
    link = Field()
    content = Field()
    source = Field()
    section = Field()
    keyword = Field()
    image_urls = Field()
#   images = Field()   

