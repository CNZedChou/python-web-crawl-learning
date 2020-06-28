# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  19_reg_greedy2.py
@Description    :  
@CreateTime     :  2020-4-25 20:08
------------------------------------
@ModifyTime     :  
"""
import re
s = 'aa<div>test1</div>bb<div>test2</div>cc'
pattern1 = re.compile('<div>.*?</div>')
pattern2 = re.compile('<div>.*</div>')
result1 = pattern1.findall(s)
result2 = pattern2.findall(s)
print(result1) # ['<div>test1</div>bb<div>test2</div>']
print(result2) # ['<div>test1</div>bb<div>test2</div>']