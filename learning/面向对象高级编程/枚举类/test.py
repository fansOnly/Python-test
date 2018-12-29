#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# 使用枚举类
#############################################################################
# Enum枚举类
# from enum import Enum

# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# for name, member in Month.__members__.items():
#     print(name, '=>', member, '=>', member.value)


#############################################################################
# @unique装饰器可以帮助我们检查保证没有重复值。
# from enum import Enum, unique

# @unique
# class Weekday(Enum):
#     Sun = 0
#     Mon = 1
#     Tue = 2
#     Wed = 3
#     Thu = 4
#     Fri = 5
#     Sat = 6
# print(Weekday.Mon)
# print(Weekday['Wed'])
# print(Weekday(5).value)


#############################################################################
# 练习
# 把Student的gender属性改造为枚举类型，可以避免使用字符串：
from enum import Enum, unique
@unique
class Gender(Enum):
    Male = 0
    Female = 1
class Student(object):
    def __init__(self, name, gender):
        self._name = name
        self._gender = gender
bart = Student('Bart', Gender.Male)
print(bart._gender)