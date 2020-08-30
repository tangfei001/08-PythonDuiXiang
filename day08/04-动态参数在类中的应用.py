#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 9:18
# @Author  : Aries
# @Site    : 
# @File    : 04-动态参数在类中的应用.py
# @Software: PyCharm

class Person(object):
	#动态参数在类中的应用
	def __init__(self,*args,**kwargs):
		self.args=args
		self.kwargs=kwargs

	def info(self):
		print(u'信息是{0},第二个值是{1}'.format(self.args,self.kwargs.values()))

#创建对象
per1=Person(5,{'name':'tangfei','age':25})
per1.info()
per2=Person(name='tangfei',age=25)
per2.info()