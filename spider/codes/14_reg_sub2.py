# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  14_reg_sub2.py
@Description    :  
@CreateTime     :  2020-4-25 14:59
------------------------------------
@ModifyTime     :  
"""
import re
p = re.compile(r'(\w+) (\w+)')
s = 'hello 123,hello 456'
def func(m):
    print(m.group(2))
    return 'hi'+' '+m.group(2)
print(p.sub(func,s))
print(p.sub(func,s,1))
