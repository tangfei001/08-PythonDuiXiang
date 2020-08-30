#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 9:55
# @Author  : Aries
# @Site    : 
# @File    : 12-实例属性的继承.py
# @Software: PyCharm

'''
子类由于业务的需求,需要继承父类的实例属性

格式: Fruit.__init__(self,name)
'''
#父类
class Fruit(object):
	#父类的实例属性
	def __init__(self,name):
		self.name=name

#子类
class Apple(Fruit):
	#子类的实例属性
	def __init__(self,name,brand,color):
		#子类由于业务需要,需要继承父类的实例属性
		Fruit.__init__(self,name)
		self.brand=brand
		self.color=color

	def inao(self):
		print('名字是:{0},品牌:{1},颜色:{2}'.format(self.name,self.brand,self.color))

#创建对象并打印结果
apple=Apple('苹果','品牌','红色')
apple.inao()



