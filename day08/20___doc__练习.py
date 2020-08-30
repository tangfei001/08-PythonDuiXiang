#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 10:29
# @Author  : Aries
# @Site    : 
# @File    : 20___doc__练习.py
# @Software: PyCharm

'''
__doc__ 打印出类的注释
调用的格式: xxx.__doc__ xxx:类名
举例:Person.__doc__

'''

class Person(object):
	'''定义一个类,类名叫Person'''
	def info(self,username,password):
		pass

#打印出类的注释
print(Person.__doc__)