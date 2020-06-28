# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  12_reg_test.py
@Description    :  
@CreateTime     :  2020-4-25 14:30
------------------------------------
@ModifyTime     :  
"""
import re

nums = ['0','-100','20','19']
p1 = re.compile(r'^\d+$') # 匹配非负整数
p2 = re.compile(r'^[1-9]\d*$') # 匹配正整数
p3 = re.compile(r'[0-]\d*$') # 匹配非正整数
for num in nums:
    print(p1.search(num))
    print('------------')
    print(p2.search(num))
    print('------------')
    print(p3.search(num))
