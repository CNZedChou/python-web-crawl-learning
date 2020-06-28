# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  18_reg_chinese.py
@Description    :  
@CreateTime     :  2020-4-25 19:51
------------------------------------
@ModifyTime     :  
"""
import re
title = '你好,hello,世界'
pattern = re.compile('[\u4e00-\u9fa5]+')
result = pattern.findall(title)
print(result)