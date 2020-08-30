#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 9:27
# @Author  : Aries
# @Site    : 
# @File    : 06-oop对象调用方法的执行顺序.py
# @Software: PyCharm

'''
__init__(self) 构造函数

__del__(self)  构细函数

对象(类的实例化)--类的构造函数--执行的是调用的方法-最后执行析构方法
'''
class Person(object):

	#我是构造函数
	def __init__(self):
		print('我是构造函数')
	#我是构析函数
	def __del__(self):
		print('我是构析函数')
	#我是普通方法
	def a(self):
		print('我是普通方法')

per1=Person()
per1.a()
