# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  myDownloadMiddleWares.py
@Description    :  
@CreateTime     :  2020-6-27 20:53
------------------------------------
@ModifyTime     :  
"""
from selenium import webdriver
from scrapy.http import HtmlResponse

class TencentDownload(object):
    def __init__(self):
        pass

    def process_request(self,request,spider):
        '''
        实现自定义下载
        :param request:
        :param spider:
        :return:None:继续处理这个请求，也就是说这个请求会被下载器下载
                IgnoreRequest：忽略这条请求，在增量爬虫中，我们可以通过对已经下载过的请求这样处理来停止对这条请求的下载
                response：htmlresponse此时下载器看到这个对象，就认为这个request就已经被下载了，就不会自己下载
        '''
        # print("in middleware")
        driver = webdriver.PhantomJS()
        driver.get(request.url)
        # 等待
        driver.implicitly_wait(10)
        # 获取页面内容
        html_str = driver.page_source
        return HtmlResponse(url=request.url,body=html_str,encoding='utf-8',request=request)
