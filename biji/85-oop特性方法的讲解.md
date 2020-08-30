**85-oop特性方法的讲解**

特性方法:不能有形式参数

注意:调用的时候不需要带括号

引用:@property

class Person(object):
	@property
	def getUserId(self):
		pass
per=Person()
per.getUserId

# from selenium import  webdriver
# driver=webdriver.Firefox()
# driver.find_element_by_id('').text

特性方法的特征

01:引用 @property

02:没有形式参数, def getUserId(self)

03:调用的时候不需要带括号 per.getUserId

