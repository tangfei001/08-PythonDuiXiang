#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 10:25
# @Author  : Aries
# @Site    : 
# @File    : 18-工厂设计模式.py
# @Software: PyCharm

class Factory(object):
	def createFruit(self,fruit):
		if fruit=='apple':
			return Apple()
		elif fruit=='banana':
			return Banana()

class Fruit(object):
	def __str__(self):
		return 'fruit'

class Apple(Fruit):
	def __str__(self):
		return 'apple'

class Banana(Fruit):
	def __str__(self):
		return 'banana'

if __name__ == '__main__':
	factory=Factory()
	print(factory.createFruit('apple'))
	print(factory.createFruit('banana'))
