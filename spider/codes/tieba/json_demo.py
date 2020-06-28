# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  json_demo.py
@Description    :  
@CreateTime     :  2020-4-19 22:57
------------------------------------
@ModifyTime     :  
"""
import json
json_data = {'abc':0,'cc':[1,2,3,4,5]}
json_str = json.dumps(json_data)
print(json_str)
print(json_data)