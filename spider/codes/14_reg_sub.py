# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  14_reg_sub.py
@Description    :  
@CreateTime     :  2020-4-25 14:51
------------------------------------
@ModifyTime     :  
"""
import re
p = re.compile(r'(\w+) (\w+)')
s = 'hello 123,hello 456'
# 提前用p区匹配目标串，找到能匹配出来的内容，就是替换找出来的这个内容
print(p.sub(r'hello world',s)) # 使用hello world 来替换hello 123 和hello 456
print(p.sub(r'\2 \1',s)) # 引用分组