# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  09reg_match2.py
@Description    :  
@CreateTime     :  2020-4-23 15:43
------------------------------------
@ModifyTime     :  
"""
import re
pattern = re.compile(r'([a-z]+) ([a-z]+)',re.I) # re.I 表示忽略大小写
m = pattern.match('Hello World Python Spider')
print(m)
# group(1),group(2) 返回一个分组情况，group(0) 是整个匹配
print(m.group()) # Hello World
print(m.span(1)) # 取1分组的匹配范围 (0, 5)