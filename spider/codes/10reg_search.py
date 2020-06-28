# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  10reg_search.py
@Description    :  
@CreateTime     :  2020-4-23 16:47
------------------------------------
@ModifyTime     :  
"""
import re
pattern = re.compile(r'\d+')
content = 'one12twothree34four'
# 全文匹配，只匹配一次，返回一个match对象
m = pattern.search(content)
print(m)
# <_sre.SRE_Match object; span=(3, 5), match='12'>
m = pattern.search(content,10,30)
print(m)
# <_sre.SRE_Match object; span=(13, 15), match='34'>
content2 = 'hello 123456 789'
m = pattern.search(content2)
if m :
    print(m.group()) # 123456
