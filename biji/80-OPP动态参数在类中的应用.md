**80-OPP动态参数在类中的应用**

class Person(object):
	def __init__(self,**kwargs):
		self.kwargs=kwargs
		self.args=args
	def info(self):
		print(u'信息是:',self.kwargs.values())

per1=Person(name='wuya')
per1.info()
per2=Person(name='wuya',age=18)
per2.info()
per3=Person(name='wuya',age=18,ismarry='masrry')
per3.info()