#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 10:25
# @Author  : Aries
# @Site    : 
# @File    : 19-登录案例实战.py
# @Software: PyCharm

'''
任务:使用类完成登录实战
思路
登录类:
	:定义两个实例属性用户名和密码
	:使用get 和set方法进行
	:注册函数
	:登录函数
	:获取用户名的函数
	:退出函数
主函数
	:实例化
	:死循环
		:异常处理
		:异常中添加逻辑
if __name__ =='__main__':
	mian()

'''
#使用json库
import json
import sys
#定义一个类,类名叫Login()
class Login(object):
	'''
	01:类中有两个实例属性用户名和密码
	02:使用构造函数进行初始化
	03:使用get()和set()函数进行设置
	'''
	def __init__(self,username,password):
		self.username=username
		self.password=password

	def getUsername(self):
		return self.username
	def setUsername(self,username):
		self.username=username
	def getPassword(self):
		return self.password
	def setPassword(self,password):
		self.password=password

	#写一个注册函数,函数名叫zhuce()
	def zhuce(self):
		#使用文件的序列化写入文件
		temp=self.username+'|'+self.password
		json.dump(temp,open('login.md','w'))
		print('恭喜您注册成功')

	#写登陆函数,函数名叫denglu()
	def denglu(self):
		#使用文件的反序列化读取文件,需要定义一个变量info
		info=str(json.load(open('login.md','r')))
		#吧字符串info转化为列表 info.split
		info=info.split('|')
		#使用if语句进行判断,成功返回True失败返回False
		if info[0]==self.username and info[1]==self.password:
			return True
		else:
			return False

	#写获取昵称的函数,函数名叫nicheng()
	def nicheng(self):
		#使用文件的反序列化读取文件中的用户名,需要定义一个变量info
		info=str(json.load(open('login.md','r')))
		#将字符串infao转化为列表
		info=info.split('|')
		#定义一个变量r,吧登录函数作为参数传入
		r=self.denglu()
		#进行判断,成功弹出提示信息(欢迎您访问我的个人主页),失败提示用户
		if r:
			print('欢迎{0}访问我的个人主页'.format(info[0]))
		else:
			print('获取信息失败,请检查用户名和密码是否输入正确')

	#写一个退出函数exit()
	def exit(self):
		sys.exit(1)

#定义一个主函数,函数名叫做main()
def main():
	#对类Login()进行实例化(创建对象并实例化)
	user=Login('tangfei','123456')
	#写一个死循环
	while True:
		'''
		01:使用异常的知识对用户输入进行处理
		02:在异常中嵌入代码
		'''
		try:
			#对用户输入进行处理
			t=int(input('1,注册 2,登录 3,退出系统\n'))
			#对用户的输入进行判断,浮点 和字符串
			if isinstance(t,float):
				t=int(t)
			elif isinstance(t,str):
				if len(t)==1:
					t=ord(t)
				else:
					t=int(ord(list[t][0]))
		except Exception as e:
			print(e.args)
			print('请输出1或者2或者3')
		else:
			#实现的功能
			if t==1:
				user.zhuce()
			elif t==2:
				user.nicheng()
			elif t==3:
				exit(1)
			else:
				print('登录失败请检查用户名和密码')
		finally:pass
#调用主函数
if __name__ == '__main__':
    main()

