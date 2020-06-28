# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  08reg_python.py
@Description    :  
@CreateTime     :  2020-4-23 15:27
------------------------------------
@ModifyTime     :  
"""
import re
# 例如我们需要打印出c:\a\b\c
# 正斜杠/
# 反斜杠\ 表示转义字符
path1 = 'c:\a\b\c'
print(path1) # c:\c
path2 = 'c:\\a\\b\\c' # c:\a\b\c
print(path2)
path3 = r'c:\\a\\b\\c' # c:\\a\\b\\c ,r的作用是输出原字符串
print(path3)
