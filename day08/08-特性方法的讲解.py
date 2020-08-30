#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 9:40
# @Author  : Aries
# @Site    : 
# @File    : 08-特性方法的讲解.py
# @Software: PyCharm

'''
01:引用 @property
02:没有形式参数, def getUserId(self)
03:调用的时候不需要带括号 per.getUserId
'''
class Person(object):
	@property
	def conn(self):
		print('我是特性方法')
per1=Person()
#注意调用的格式-没有括号
per1.conn