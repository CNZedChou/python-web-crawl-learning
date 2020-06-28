# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  19_reg_greedy.py
@Description    :  
@CreateTime     :  2020-4-25 19:55
------------------------------------
@ModifyTime     :  
"""
import re
pattern = re.compile(r'ab*')
pattern2 = re.compile(r'ab*?')
pattern3 = re.compile(r'ab??') # 第一个问号表示数量控制符
result = pattern.findall('abbbc')
result2 = pattern2.findall('abbbc')
result3 = pattern3.findall('abbbc')
print(result)
print(result2)
print(result3)
