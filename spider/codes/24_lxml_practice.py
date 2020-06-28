# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  24_lxml_practice.py
@Description    :  
@CreateTime     :  2020-4-29 15:06
------------------------------------
@ModifyTime     :  
"""
from lxml import etree
text = '''
<div>
    <ul>
        <li class="item-0"><a href="link1.html" class = "a_class1">first item</a></li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-inactive">
         <a href="link3.html" class="bold"></a>
         <span class="span_item1">span_text1</span>
      </li>
        <li class="item-1">
            test
         <a href="link4.html">fourth item<span class="span_item2">span_text2</span></a>
      </li>
        <li class="item-0">
         <a href="link5.html">fifth item</a>
    </ul>

</div>
'''
# 1.将html_str --》html（element对象）
html = etree.HTML(text)
# 获取所有的li标签
li_list = html.xpath('//ul/li')
# 继续获取li标签的所有class属性
for li in li_list:
    li_class = li.xpath('./@class') # li 标签的所有class属性
    # print(li_class)

li_classes = html.xpath('//ul/li/@class')

# 继续获取li标签下href 为link1.html的a 标签
a = html.xpath('//ul/li/a[@href="link1.html"]')

# 过去li标签下的所有的span标签（包括孙子span）
span = html.xpath('//li//span')

# 获取li标签下a标签里的所有class
class_a = html.xpath('//li/a/@class')

# 获取最后一个li标签中的a标签中的href
last_a = html.xpath('//ul/li[last()]/a/@href')

# 获取倒数第二个元素的内容
result = html.xpath('//*[last()-1]/text()')

# 获取class 值为bold的标签名
bold = html.xpath('//*[@class="bold"]')[0]
print(bold.tag)