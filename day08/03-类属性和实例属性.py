#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 9:03
# @Author  : Aries
# @Site    : 
# @File    : 03-类属性和实例属性.py
# @Software: PyCharm

class Person(object):
	#类属性
	guoji='china'
	def __init__(self,name,age):
		#实例属性
		self.name=name
		self.age=age
	#写几个方法
	def getName(self):
		return self.name
	def setName(self):
		self.name=name
	def getAge(self):
		return self.age
	def setAge(self):
		self.age=age
	#对上面的函数进行整合
	def info(self):
		print('名字是:{0},年龄是:{1},国籍是:{2}'.format(self.name,self.age,self.guoji))

#创建对象
per1=Person('wuya',25)
per2=Person('tang',25)
#创建对象2
per1.info()
per2.info()
#类属性可以直接用类名调用
print(Person.guoji)