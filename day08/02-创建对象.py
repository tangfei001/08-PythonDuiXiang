#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 8:59
# @Author  : Aries
# @Site    : 
# @File    : 02-创建对象.py
# @Software: PyCharm

'''
对象的创建--->就是类实例化的过程
1.对象的句柄-->区分不同的对象
'''
class Person(object):
	def a(self):
		print('我是一个普通方法')

#创建对象1
person1=Person()
person1.a()
#创建对象2
person2=Person()
person2.a()