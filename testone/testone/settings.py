# Scrapy settings for testone project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

import os
import sys



PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
os.path.join(PROJECT_DIR,'pipedir')

sys.path.insert(0,PROJECT_DIR+"/pipedir/images")

DOWNLOAD_DELAY = 0.5

BOT_NAME = 'testone'

SPIDER_MODULES = ['testone.spiders']
NEWSPIDER_MODULE = 'testone.spiders'

IMAGES_STORE = 'downloaded-image/'
IMAGES_MIN_HEIGHT = 200
IMAGES_MIN_WIDTH = 200
ITEM_PIPELINES = ['testone.img_pipelines.ImageDownloaderPipeline',
                'testone.article_pipelines.TestonePipeline',
               ]
#ITEM_PIPELINES = ['testone.article_pipelines.TestonePipeline']
EXTENSIONS = {'testone.myext.myExt':500}

LOG_ENABLED = True
LOG_ENCODING = 'utf-8'
LOG_FILE = './crawl.log'
LOG_LEVEL = 'DEBUG'
LOG_STDOUT = False

#DUPEFILTER_CLASS = ['testone.dupefilter']
