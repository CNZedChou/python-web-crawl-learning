# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  11reg_findall.py
@Description    :  
@CreateTime     :  2020-4-23 16:56
------------------------------------
@ModifyTime     :  
"""
import re
pattern = re.compile('we')
m = pattern.findall('we work well ,welcome')
print(m) # ['we', 'we', 'we']
pattern = re.compile('(w)(e)')
# findall 配合分组，他只会取分组中的内容放入元组，list 中存储的就是所有的元组
m = pattern.findall('we work well,welcome')
print(m) # [('w', 'e'), ('w', 'e'), ('w', 'e')]
pattern = re.compile('(w)e')
m = pattern.findall('we work well,welcome')
print(m) # ['w', 'w', 'w']