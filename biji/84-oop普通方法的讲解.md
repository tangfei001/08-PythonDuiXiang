**84-oop普通方法的讲解**

class Person(object):
	#写第一个普通方法
	def conn(self,uesr,password,host,port):
		pass
	#写第二个普通方法
	def f1(self,*args,**kwargs):
		pass
	#写第三个普通方法
	def info(self):
		print(u'我是普通方法')

#对类进行实例化
per=Person()
per.conn('wuya','srver','localhost',3306)
per.f1()
per.f1('admin')
per.f1(name='tangfei')