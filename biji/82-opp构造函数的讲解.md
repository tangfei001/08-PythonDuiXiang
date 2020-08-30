**82-opp构造函数的讲解**
01-首先一个类，不管是否写了构造函数，它都是有构造函数的
02-一个类，可以有多个构造函数,建议一个类只有一个构造函数


构造函数:初始化属性

class Person(object):
	def __init__(self,name,age):
		self.name=name
		self.age=age

per=Person('先',18)


析构函数

def __del__()