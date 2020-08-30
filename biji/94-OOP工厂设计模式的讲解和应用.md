**94-OOP工厂设计模式的讲解和应用**

# 01:__doc__ 打印出类的注释 # 

调用的格式: xxx.__doc__ xxx:类名
举例:Person.__doc__

class Person(object):
	'''定义一个类,类名为人类'''
	def info(self,username,password):
		'''
		:param username: 用户名
		:param password: 密码
		'''
		pass
print(Person.__doc__)


# 02:'''__new__:对象创建时直接返回__call__的内容,使用该方法可以模拟静态方法'''   __new__方法

class Person(object):
	'''定义一个类,类名叫人列'''
	def __new__(cls, *args, **kwargs):
		print('打印call的方法')

per=Person()

# 03:__str__:对象代表的含义，返回一个字符串,通过它可以把对象和字符串关联起来，方便某些程序的实现,
该字符串表示某个类,实现了__str__后，可以直接使用print语句输出对象,也可以通过函数str来触发__str__的执行  __str__方法 #

1.对象的意思
2.返回一个字符串，字符串和对象关联起来-->该字符串表示某个类

class Person(object):
	'''定义一个类,类名叫人'''
	def __str__(self):
		return self.__doc__

per=Person()
print(str(per))

-----------------------------------------------------
class Factory(object):
	#创建水果这个方法-必须有一个参数
	def createFruit(self,fruit):
		if fruit=='苹果':
			return Apple()
		elif fruit=='香蕉':
			return Banana()

class Fruit(object):
	def __str__(self):
		return 'fruit'

class Apple(Fruit):
	def __str__(self):
		return '苹果'

class Banana(Fruit):
	def __str__(self):
		return '香蕉'

if __name__=='__main__':
	factory=Factory()
	print(factory.createFruit('苹果'))
	print(factory.createFruit('香蕉'))