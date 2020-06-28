# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import hashlib

import pymongo


class BiqugePipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient()
        self.db = self.client['biquge']

    def get_md5(self,value):
        md5 = hashlib.md5(bytes(value,encoding='utf-8'))
        return md5.hexdigest()

    def process_item(self, item, spider):
        # 按照什么条件更新
        # db.c.update({查询表达式},{更新成什么},{update:ture})
        # 使用hash进行查找，在item中添加hash_url字段
        item['hash_url'] = self.get_md5(item['chapter_url'])
        self.db['xuanhuan'].update({'hash_url':item['hash_url']},{'$set':dict(item)},True)
        print(item['hash_url'])
        return item

