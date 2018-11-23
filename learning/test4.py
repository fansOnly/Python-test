#!user/bin/env python3
#-*- coding: utf-8 -*-

# 定制类
##################################################################################

# __str__ __repr__

# class Student(object):
#     def __init__(self, name):
#         self.name = name
#     def __str__(self):
#         return 'Student name is: %s' % self.name
#     __repr__ = __str__

# s = Student('Machil')
# print(s)
# print(s.name)

# *********************************************
# __iter__
# 该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
# 斐波那契数列
# class Fib(object):
#     def __init__(self):
#         self.a, self.b = 0, 1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b
#         if self.a > 1000:
#             raise StopInteration()
#         return self.a, self.b
# for n in Fib():
#     print(n)

# *********************************************
# __getitem__
# class Fib(object):
# 	def __getitem__(self, n):
# 		if isinstance(n, int):
# 			a, b = 1, 1
# 			for x in range(n):
# 				a, b = b, a + b
# 			return a
# 		if isinstance(n, slice):
# 			start = n.start
# 			stop = n.stop
# 			if start is None:
# 				start = 0
# 			a, b = 1, 1
# 			L = []
# 			for x in range(stop):
# 				if x >= start:
# 					L.append(a)
# 				a, b = b, a + b
# 			return L
# f = Fib()
# print(f[10])
# print(f[0:5])

# *********************************************
# __getattr__

# *********************************************
# class Student(object):
# 	def __init__(self):
# 		self.name = 'Michael'
# 	def __getattr__(self, attr):
# 		if attr == 'age':
# 			return 50
# 		raise AttributeError('\'Student\' do not has attribute \'%s\'' % attr)

# s = Student()
# print(s.name)
# print(s.age)
# print(s.agexxxxx)

# *********************************************
# REST API
# class Chain(object):
# 	def __init__(self, path=''):
# 		self._path = path
# 	def __getattr__(self, path):
# 		return Chain('%s/%s' % (self._path, path))
# 	def __str__(self):
# 		return self._path
# 	__repr__ = __str__

# url = Chain().status.user.list
# print(url)

# *********************************************
class Chain(object):
	def __init__(self, path=''):
		self._path = path
	def __getattr__(self, path):
		if path.index('(') and path.index(')'):
			start = path.index('(')
			end = path.index(')')
			return Chain('%s/%s/:%s' % (self._path, path[0 : start], path[start+1 : end - 1]))
		else:
			return Chain('%s/%s' % (self._path, path))
	def __str__(self):
		return self._path
	__repr__ = __str__

url = Chain().status.users('Michael').list
print(url)

# __call__
# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用
# *********************************************
# class Student(object):
# 	def __init__(self, name):
# 		self._name = name
# 	def __call__(self):
# 		print('my name is %s' % self._name)
# s = Student('Michael')
# s()


# print(callable(Student))
# print(callable([1,2,3]))
# print(callable('123'))