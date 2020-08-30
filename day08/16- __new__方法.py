#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 10:24
# @Author  : Aries
# @Site    : 
# @File    : 16- __new__方法.py
# @Software: PyCharm

'''
__new__:对象创建时直接返回__call__的内容,使用该方法可以模拟静态方法
'''
class Person(object):
	'''定义一个类,类名叫Person'''
	def __new__(cls, *args, **kwargs):
		print('打印出我的方法')
#创建对象
per1=Person()