**87-oop类方法的讲解**


类方法:直接使用类进行调用它属于类

引用: 	@classmethod

class Person(object):
	@classmethod
	def conn(cls):
		pass


类方法的特征:


01:引用@classmethod

02:直接使用类进行调用

03:没有self参数.是cls参数
