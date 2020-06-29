# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  my_middleware.py
@Description    :  
@CreateTime     :  2020-6-29 17:44
------------------------------------
@ModifyTime     :  
"""
from selenium import webdriver
from scrapy.http import HtmlResponse


class MyMiddleWares(object):
    def __init__(self):
        pass
    def process_request(self,request,spider):
        """
        默认使用selenium
        用下载器下载的请求，meta={flag=True}
        :param request:
        :param spider:
        :return:
        """
        if not request.meta['flag']:
            # 使用selenium
            driver = webdriver.Chrome()
            driver.get(request.url)
            driver.implicitly_wait(10)
            html_str = driver.page_source
            driver.quit()
            return HtmlResponse(url = request.url, body = html_str,encoding='utf-8',request=request)
        else:
            return None