#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 9:55
# @Author  : Aries
# @Site    : 
# @File    : 14-多个类的继承.py
# @Software: PyCharm

'''
从左到右的原则
'''
#父类
class Person(object):
	def eat(self):
		print('人要吃饭')

#第一及子类
class Father(Person):
	# def eat(self):
	# 	print('父亲喜欢吃肉')
	pass
#第一级子类
class Mother(Person):
	def eat(self):
		print('母亲喜欢吃菜')

#第二级子类-同时继承第一集子类
class Son(Father,Mother):
	pass

son=Son()
son.eat()

