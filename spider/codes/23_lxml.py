# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  23_lxml.py
@Description    :  
@CreateTime     :  2020-4-29 12:58
------------------------------------
@ModifyTime     :  
"""
from lxml import etree

text = """
<div>
    <ul>
        <li class="item-0"><a href="link1.html">first item</a><li>
        <li class="item-1"><a href="link2.html">second item</a><li>
        <li class="item-inactive"><a href="link3.html">third item</a><li>
        <li class="item-1"><a href="link4.html">fourth item</a><li>
        <li class="item-0"><a href="link5.html">fifth item</a><li>
    </ul>
</div>
"""
# lxml 的使用方法
# 将xml 或者html 解析成element 对象
# 使用html的方式进行解析
# 如果内容在没有html的标签，就会自动补全
html = etree.HTML(text)
# print(html) # <Element html at 0x21668ef7648>
# 如何将element对象变成字符串
# print(etree.tostring(html,pretty_print=True).decode('utf-8'))
# 1.element 对象有xpath方法，可以写xpath语法进行筛选数据
# 2.这个对象可以继续使用xpath进行选取
# xpath方法返回的是一个list，里面存储的是筛选出来的所有内容
ul = html.xpath('//ul')[0]
# 选取ul标签下的第一个li
li_first = ul.xpath('.//li[1]')
# print(li_first)
# 选取属性
li_class = html.xpath('//ul/li[1]/@class')
# print(li_class)

# 选取属性
a_text = html.xpath('//ul/li[1]/a/text()')
print(a_text)