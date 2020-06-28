# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class MaoyanPipeline(object):
    def __init__(self):
        # mongo 连接
        self.client = pymongo.MongoClient()
        self.db = self.client['maoyan']
    def process_item(self, item, spider):
        # 将数据插入到数据库中
        # insert方法需要插入一个字典，所以需要强转
        self.db['movie'].insert(dict(item))
        # 之所以return是将item交给其他管道，如果只有一个，这item就处理完成了，在spider中就可以yield下一个
        return item
