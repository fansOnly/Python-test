#!usr/bin/env python3
#-*- coding: utf-8 -*-


# 实例属性和类属性
# class Student(object):
#     name = 'student'

# s = Student()

# print(s.name)
# print(Student.name)

# s.name = 'jone'
# print(s.name)
# print(Student.name)

# del s.name
# print(s.name)
# print(Student.name)

class Student(object):
    count = 0
    def __init__(self, name):
        self.name = name
        Student.count += 1
if Student.count != 0:
    print('err 1')
else:
    Zara = Student('zara')
    if Student.count != 1:
        print('err 2')
    else:
        Ur = Student('ur')
        if Student.count != 2:
            print('err 3')
        else:
            print('success %s' % Student.count)