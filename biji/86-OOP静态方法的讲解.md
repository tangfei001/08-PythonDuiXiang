**86-OOP静态方法的讲解**

静态方法:直接使用类名来进行调用他属于对象,也可以调用静态方法,但是一般不建议这样做

注意:静态方法没有self参数

引用:@staticmethod

class MySql(object):
	@staticmethod
	def conn(uesr):
		pass

#静态方法可以直接使用类名进行调用
MySql.conn('WUYA')


静态方法的特征

01:引用 @staticmethod

02:没有self参数,需自己定义一个参数 def conn(uesr)

03:调用的时候直接使用类名来进行调用  per.conn('duod')
