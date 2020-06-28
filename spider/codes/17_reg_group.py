# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  17_reg_group.py
@Description    :  
@CreateTime     :  2020-4-25 17:23
------------------------------------
@ModifyTime     :  
"""
import re
content = '{name:"zhangsan",age:"10",hobby:["basketball","football","read"]}'
pattern = re.compile(r'name:"(\w+)",age:"(\d+)".+')
# 正则使用技巧：券串匹配，使用分组获取特定内容，括号两边的边界一定要指定
match = pattern.search(content)
print(match.group(0))
print(match.group(1))
print(match.group(2))