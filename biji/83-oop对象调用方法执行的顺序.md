**oop对象调用方法执行的顺序**

析构函数


执行的顺序

对象(类的实例化)--类的构造函数--执行的是调用的方法-最后执行析构方法

class Person(object):
	#构造函数
	def __init__(self):
		print(u'我是构造函数')
	#析构函数
	def __del__(self):
		print(u'我是析构函数')
	#方法
	def info(self):
		print(u'我是方法')

#对类进行实例化
per1=Person()
per1.info()
