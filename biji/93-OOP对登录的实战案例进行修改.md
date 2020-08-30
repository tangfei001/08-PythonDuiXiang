**93-OOP对登录的实战案例进行修改**

#需要引入json库
import json
#定义一个类,里面有用户名和密码
class Login(object):
	#写一个构造函数,两个实例属性用户名和密码
	def __init__(self,username,password):
		self.username=username
		self.password=password
	#对这个两个实例属性进行设置
	def getUsername(self):
		return self.username
	def setUsername(self,username):
		self.username=username
	def getPassword(self):
		return self.password
	def setPassword(self,password):
		self.password=password

	#注册函数
	def zhuce(self):
		#文件的序列化写入文件
		temp=self.username + '|' +self.password
		json.dump(temp,open('login2.md','w'))

	#写登陆函数
	def denglu(self):
		#文件的反序列化获取文件
		info=str(json.load(open('login2.md','r')))
		#因为获取到的用户名和密码是字符串,需要我们转换为列表
		info=info.split('|')
		#进行判断
		if info[0]==self.username and info[1]==self.password:
			return True
		else:
			return False
	#获取昵称的函数
	def nicheng(self):
		#文件反序列化获取内容
		info=str(json.load(open('login2.md','r')))
		#跟登陆一言
		info=info.split('|')
		#调用登陆函数
		r=self.denglu()
		#进行判断
		if r:
			print('欢迎{0}访问我的个人主页'.format(info[0]))
		else:
			print('登陆失败,请检查用户名和密码是否有错误')

	#写一个退出函数
	def exit(self):
		sys.exit(1)

def main():
	#对类进行初始化
	per=Login('唐飞','123456')
	#写一个死循环
	while True:
		#使用异常的知识
		try:
			t=int(input('1,注册 2,登录 3,退出系统\n'))
			if isinstance(t,float):
				t=int(t)
			elif isinstance(t,str):
				if len(t)==1:
					t=ord(t)
				else:
					t=int(ord(list(t)[0]))
		except Exception as e:
			print(e.args)
		else:
			if t==1:
				per.zhuce()
			elif t==2:
				per.nicheng()
			elif t==3:
				exit(1)
			else:
				print('输入有误请重新输入')
		finally:pass

#调用主函数
if __name__ == '__main__':
	main()