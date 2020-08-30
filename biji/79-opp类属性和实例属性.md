**79-opp类属性和实例属性**

1.对象的句柄-->区分不同的对象

对象的第二个特性-属性

共有属性
	类属性(共有的部分分离出来):他属于类,也属于对象,建议使用类调用
	实例属性:它只属于对象
	局部变量
私有属性

class Person(object):
	#类的属性
	gongtong='china'
	#构造函数
	def __init__(self,name,age):
		#实例属性
		self.name=name
		self.age=age
	#写几个函数 get() set()
	def getName(self):
		return self.name
	def getAge(self):
		return self.age
	def setName(self,name):
		self.name=name
	def setAge(self,age):
		self.age=age
	#写一个函数同时获取姓名和年龄
	def info(self):
		return 'name:{0},age{1,},来自:{3}'.format(self.getName(),self.getAge(),self.gongtong)

#创建对象
per1=Person('wuya',25)
per2=Person('tangfei',24)
#问题:第二个重新修改
per2.setName('lisi')
per2.setAge(25)
#获取对应的值
print(per2.info())
#类属性可以直接调用
print(Person.gongtong)