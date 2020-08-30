**课时78-OPP类的定义**

类:是由一系列属性和方法组成的

class F1(object):
	pass

对象的创建-就是类实例化的过程
三个特性
1.对象的句柄-区分不同的对象
f2=F1()
f1=F1()
print id(f1)
print id(f2)

实例化的格式

class F2(object):
	pass

f3=F2()