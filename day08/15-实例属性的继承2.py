#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 10:00
# @Author  : Aries
# @Site    : 
# @File    : 15-实例属性的继承2.py
# @Software: PyCharm

#父类
class Fruit(object):
	def __init__(self,name):
		self.name=name

#子类
class Apple(Fruit):
	def __init__(self,brand,color):
		self.brand=brand
		self.color=color

	def indo(self):
		print('品牌:{0},颜色:{1}'.format(self.brand,self.color))

apple=Apple('PINPAI','红色')

apple.indo()