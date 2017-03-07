# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import traceback
import pymongo
from scrapy.conf import settings
from eastmoney.items import EastmoneyItem

class EastmoneyPipeline(object):
    def __init__(self):
        host=settings['MONGODB_HOST']
        port=settings['MONGODB_PORT']
        db_name=settings['MONGODB_DBNAME']
        client=pymongo.MongoClient(host=host,port=port)
        db=client[db_name]
        db.authenticate('tianmin','2386043')
        self.post=db[settings['MONGODB_DOCNAME']] 
    def process_item(self, item, spider):
        if isinstance(item,EastmoneyItem):
            try:
                stock_info=dict(item)
                if self.post.insert(stock_info):
                    print("存入数据")
            except Exception as e:
                print("出现错误")
                traceback.print_exception()
                
                
        return item
