# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  23_lxml2.py
@Description    :  
@CreateTime     :  2020-4-29 13:31
------------------------------------
"""
from lxml import etree

# parse() 按照xml的语法要求来解析
tree = etree.parse('a.html')
print(tree)