# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  16_reg_split.py
@Description    :  
@CreateTime     :  2020-4-25 17:20
------------------------------------
@ModifyTime     :  
"""
import re
p = re.compile(r'[\s\,\;]+')
a = p.split('a,b;;c   d')
print(a)