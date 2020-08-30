#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 9:45
# @Author  : Aries
# @Site    : 
# @File    : 09-静态方法的讲解.py
# @Software: PyCharm

'''
01:引用 @staticmethod
02:没有self参数,需自己定义一个参数 def conn(uesr)
03:调用的时候直接使用类名来进行调用  per.conn('duod')
'''
class Person(object):
	@staticmethod
	def conn(age):
		print('我是静态方法')
#注意调用的格式-不需要实例化,直接使用类名进行调用
Person.conn(25)