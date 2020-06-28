# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  17_reg_group2.py
@Description    :  
@CreateTime     :  2020-4-25 19:08
------------------------------------
@ModifyTime     :  
"""
import re
s = "<html><h1>正则表达式</h1></html>"
pattern = re.compile(r'<(html)><(h1)>(.*)</\2></\1>')
# \2 表示分组2的内容 \1表示分组1的内容
match = pattern.search(s)
print(match.group(3))