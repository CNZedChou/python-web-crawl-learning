# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  49_metaclass.py
@Description    :  元类的相关内容
@CreateTime     :  2020-6-30 15:05
------------------------------------
@ModifyTime     :  
"""
"""
元类：
1. 在python中一切皆对象
2. 对象是由类创建出来的
    class A:
        pass
    obj = A()
    type(obj) -- 本质上可以查看这个对象是由哪个类创建出来的
    a.__class__ 和 type作用是一样的
3. 动态创建类
    类的创建方式：python默认提供的方式是通过class类进行创建
    自定义动态创建：type(
                    name，类的名字
                    bases，类的继承的元组
                    attrs，类的属性字典
                    )
3. 类到底是谁创建出来的？ -- 元类
    元类：创建类
    myclass = MetaClass()
    myObject = myclass()
    在python里面，这个元类就是type
4. 当一个类实例化的时候：Foo()
    __new__: 初始化这个类
    __init__: 初始化这个对象
"""
Foo = type('Foo',(),{})
print(Foo)
b = 123
print(b.__class__.__class__) # 打印b的class的class
