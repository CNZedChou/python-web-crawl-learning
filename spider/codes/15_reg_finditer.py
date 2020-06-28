# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  15_reg_finditer.py
@Description    :  
@CreateTime     :  2020-4-25 16:52
------------------------------------
@ModifyTime     :  
"""
import re
pattern = re.compile(r'\d+')
content1 = 'hello 123456 789'
content2 = 'one1two2three3four4'
result_iter1 = pattern.finditer(content1)
result_iter2 = pattern.finditer(content2,0,10) # content2 0-10

print(type(result_iter1))
print(type(result_iter2))
print('result1---------')
for m1 in result_iter1:
    print('matching string:{},position:{}'.format(m1.group(),m1.span()))
print('result2---------')
for m2 in result_iter2:
    print('matching string:{},position:{}'.format(m2.group(),m2.span()))