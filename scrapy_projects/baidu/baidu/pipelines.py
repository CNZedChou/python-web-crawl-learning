# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
'''
pipeline是管道的意思，这个管道中流淌的是item
每个管道的主要功能：对item的处理（清洗item，去重item）
    管道的功能用process_item方法处理
'''

class BaiduPipeline(object):
    def process_item(self, item, spider):
        return item
