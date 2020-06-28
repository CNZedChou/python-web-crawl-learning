# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  09reg_match.py
@Description    :  
@CreateTime     :  2020-4-23 15:34
------------------------------------
@ModifyTime     :  
"""
import re
pattern = re.compile(r'\d+') # 最少一个数字
content = 'one12twothree34four'
#mathc 默认从头开始，只匹配一次，返回一个match对象
m1 = pattern.match(content) # 从o位置开始匹配
m2 = pattern.match(content,2,10) # 从e位置开始匹配
m3 = pattern.match(content,3,10) # 从1位置开始匹配
print(m1)
print(m2)
print(m3) # <_sre.SRE_Match object; span=(3, 5), match='12'>
print(m3.group(0)) # 返回匹配的内容 12
print(m3.span()) # 范围 （3，5）
print(m3.start()) # 开始位置 3
print(m3.end()) # 结束位置 5