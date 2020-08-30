#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 9:55
# @Author  : Aries
# @Site    : 
# @File    : 13-单个类的继承.py
# @Software: PyCharm

'''
方法的继承:
1.子类为什么重写父类的方法:子类有自己的特性
当子类重写了父类的方法后，对子类进行实例化后，子类调用的方法（父类，子类都存在），执行的方法是子类的方法

单个类继承的原则：
1.从上到下：子类继承了父类，但是子类没有重写父类的方法，那么子类实例化后，调用的方法是直接调用父类当中的方法
2.从下到上的原则:子类继承了父类，但是子类重写父类的方法，那么子类实例化后，调用的方法是子类当中的方法(子类优先考虑自己类的方法)
'''
#父类
class Apple(object):
	def eat(self):
		print('水果可以吃')

#第一个子类
class ChinaApple(Apple):
	def __init__(self,color):
		self.color=color

	def eat(self):
		print('颜色是{0}的时候可以吃'.format(self.color))

#第二个子类
class UserApple(ChinaApple):
	#pass
	def eat(self):
		print('私人苹果不可以随便吃')

#创建对象并打印结果
per1=UserApple('红色')
per1.eat()