# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  main.py.py
@Description    :  
@CreateTime     :  2020-6-26 16:46
------------------------------------
@ModifyTime     :  
"""
from scrapy import cmdline
'''
使用代码来执行cmd命令
'''
cmdline.execute('scrapy crawl maoyan_spider '.split())
