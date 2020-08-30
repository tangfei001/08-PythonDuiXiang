#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 9:24
# @Author  : Aries
# @Site    : 
# @File    : 05-构造函数讲解.py
# @Software: PyCharm

'''
01-首先一个类，不管是否写了构造函数，它都是有构造函数的
02-一个类，可以有多个构造函数,建议一个类只有一个构造函数
'''
class Person(object):
	def __init__(self,age):
		self.age=age
	def info(self):
		print(self.age)

person1=Person(25)
person1.info()
