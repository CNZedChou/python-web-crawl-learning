# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  28_selenium.py
@Description    :  
@CreateTime     :  2020-5-2 15:48
------------------------------------
@ModifyTime     :  
"""
from selenium import webdriver

# 1.创建一个驱动
# driver = webdriver.PhantomJS() # 无界面
driver = webdriver.Chrome() # 有界面浏览器
# 2.请求url
driver.get('http://www.baidu.com/')
# 3.可以通过driver对象对页面进行操作
# 获取页面元素
'''
driver.find_element_by_id()# 通过id属性查找
driver.find_element_by_xpath()# 通过xpath路径查找
driver.find_element_by_css_selector()# 通过css选择器查找
'''
input_tag = driver.find_element_by_id('kw')
print(input_tag)# WebElement 对象
# WebElement 对象可以做的事情
input_tag.send_keys(u'python爬虫')
# c查看元素的位置
# print(input_tag.location)
# 查看元素大小
# print(input_tag.size)
# 截屏
# driver.save_screenshot('before_click')
# 点击操作
driver.find_element_by_xpath('//*[@id="su"]').click()
driver.close() # 关闭选项卡
driver.quit() # 关闭浏览器