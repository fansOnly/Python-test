#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#########################################################################################
# 面向对象高级编程

#########################################################################################
# 使用__slots__

# class Student(object):
#     pass

# s = Student()
# def score(self, score):
#     self.score = score
# from types import MethodType
# s.score = MethodType(score, s)
# s.score(50)
# print(s.score)


# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
# class Student(object):
#     __slots__ = ('name', 'age')

# s = Student()
# s.name = 'lily'
# print(s.name)
# s.score = 50

# class Other(Student):
#     pass

# m = Other()
# m.score = 50
# print(m.score)

#########################################################################################
# 使用@property

# class Student(object):
#     @property
#     def age(self):
#         return self._age
#     @age.setter
#     def age(self, value):
#         if not isinstance(value, int):
#             raise ValueError('age must be interval')
#         if value < 0 or value > 100:
#             raise ValueError('unvalable age')
#         self._age = value
#     @property
#     def body(self):
#         return 2015 - self._age

# s = Student()
# s.age = 80
# print(s.age)
# print(s.body)
# # s.body = 300
# s.age = 1000
# print(s.age)
# # print(s.get_age())
# # s.set_age(50)
# # print(s.get_age())
# # s.set_age(1000)
# # print(s.get_age())


class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        self._width = value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        self._height = value
    @property
    def resolution(self):
        return self._width * self._height

s = Screen()
s.width = 1024
s.height = 768
print('s.resolution', s.resolution)