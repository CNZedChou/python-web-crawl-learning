# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  14_reg_sub3.py
@Description    :  
@CreateTime     :  2020-4-25 16:37
------------------------------------
@ModifyTime     :  
"""
import re
content = 'zhangsan:2000,lisi:3000'
# zhangsan +1000
p = re.compile(r'2000')
print(p.sub('3000',content))
p2 = re.compile(r'zhangsan:(\d+)')
print(p2.sub('3000',content))
# 每个人 +1000
def func1(m):
    return 'zhangsan:'+str(int(m.group(1))+1000)
p3 = re.compile(r'(\d+)')
def func2(m):
    return str(int(m.group(1))+1000)

print(p3.sub(func2,content))
