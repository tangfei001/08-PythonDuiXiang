#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 9:36
# @Author  : Aries
# @Site    : 
# @File    : 07-普通方法的讲解.py
# @Software: PyCharm

'''
普通方法的讲解
'''
class Person(object):
	#写第一个普通方法
	def a1(self,name,age,address):
		pass
	#写第二个普通方法
	def a2(self):
		pass
	#写第三个普通方法
	def a3(self,*args,**kwargs):
		pass
per1=Person()
per1.a1('ddd',25,'sss')
per1.a2()
per1.a3(name='tangfei')