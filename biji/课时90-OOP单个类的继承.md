**课时90-OOP单个类的继承**


01:规则
 class Person(object):
	def __init__(self,name):
		self.name=name

	def info(self):
 		print self.name

 class Son(Person):
     def __init__(self,name):
	     Person.__init__(self,name)
	def info(self):
 		print self.name

s=Son('name')#注意这块内容
s.info()

'''
方法的继承:
1.子类为什么重写父类的方法:子类有自己的特性
当子类重写了父类的方法后，对子类进行实例化后，子类调用的方法（父类，子类都存在），执行的方法是子类的方法

单个类继承的原则：
1.从上到下：子类继承了父类，但是子类没有重写父类的方法，那么子类实例化后，调用的方法是直接调用父类当中的方法
2.从下到上的原则:子类继承了父类，但是子类重写父类的方法，那么子类实例化后，调用的方法是子类当中的方法(子类优先考虑自己类的方法)
'''

#第一个类
class Apple(object):
	def eat(self):
		print(u'水果是可以吃的')

#第二个类
class ChinaApple(Apple):
	def __init__(self,color):
		self.color=color

	def eat(self):
		print(u'颜色是{0}的时候可以吃'.format(self.color))

#第三个类
class UserApple(ChinaApple):
	def eat(self):
		print(u'我是用户的的水果')
	#pass

apple=UserApple(u'红色')
apple.eat()

