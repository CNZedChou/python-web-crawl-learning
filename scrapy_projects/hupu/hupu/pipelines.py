# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import hashlib


class HupuPipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient()
        self.db = self.client['hupu']

    def get_md5(self,value):
        return hashlib.md5(value.encode('utf-8')).hexdigest()
    def process_item(self, item, spider):
        item['news_id'] = self.get_md5(item['url'])
        self.db['nbanews'].update({'news_id':item['news_id']},{'$set':dict(item)},True)
        print(item)
        return item