#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 9:48
# @Author  : Aries
# @Site    : 
# @File    : 10-类方法的讲解.py
# @Software: PyCharm

'''
01:引用@classmethod
02:直接使用类进行调用
'''
class Person(object):
	@classmethod
	def conn(cls):
		print('我是类方法')

#注意调用的格式-直接使用类名进行调用
Person.conn()
