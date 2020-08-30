#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 9:55
# @Author  : Aries
# @Site    : 
# @File    : 11-类属性的继承.py
# @Software: PyCharm

'''
继承:重用已经存在的数据和行为,减少代码的重复编写
子类属性继承父类所有的实例变量和方法

关键字 父类 子类
'''
#父类
class Father(object):
	#父类属性
	guoji='china'

#子类
class Son(Father):
	pass
son1=Son()
#打印出类的属性
print(son1.guoji)