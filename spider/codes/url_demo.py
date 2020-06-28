# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  url_demo.py
@Description    :  
@CreateTime     :  2020-4-18 16:52
------------------------------------
@ModifyTime     :  
"""
from urllib import parse
url = 'https://ww.baidu.com:8888/index.html?username=222&password=123#abc'
result = parse.urlparse(url)
print(result)