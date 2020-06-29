# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import hashlib

import pymongo

class MongoPipeline(object):
    """
    在scrapy中文网上查找itempipeline 相关内容，找到其中的write item to MongoDB，利用其中的方法
    """

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        """
        爬虫启动之后，这个方法被执行
        :param crawler:
        :return:
        """
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def open_spider(self, spider):
        """
        性能意义所在：不需要写入的时候就不需要撞见mongo client
        :param spider:
        :return:
        """
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client['book']

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        item['book_id'] = self.get_md5(item['book_url'])
        self.db['book'].update({'book_id':item['book_id']},{'$set':item},True)
        print(item)
        return item

    def get_md5(self,value):
        return hashlib.md5(value.encode('utf-8')).hexdigest()

