#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 10:24
# @Author  : Aries
# @Site    : 
# @File    : 17-__str__方法.py
# @Software: PyCharm

'''
01:__str__:对象代表的含义，返回一个字符串,通过它可以把对象和字符串关联起来，方便某些程序的实现
02:该字符串表示某个类,实现了__str__后，可以直接使用print语句输出对象,也可以通过函数str来触发__str__的执行  __str__方法
1.对象的意思
2.返回一个字符串，字符串和对象关联起来-->该字符串表示某个类
'''
class Person(object):
	'''这是我随便写的'''
	def __str__(self):
		return self.__doc__
per1=Person()
print(str(per1))
