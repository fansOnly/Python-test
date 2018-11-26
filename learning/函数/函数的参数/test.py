#use/bin/env python3
#-*- coding: utf-8 -*-


# 位置参数
#######################################################################################

# def power(x):
#     return x*x

# def power2(x, n):
#     s = 1
#     while n > 0:
#         s = s * x
#         n -= 1
#     return s

# print(power2(3, 3))


# 默认参数
#######################################################################################
# 1/ 必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
# 2/ 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。

#  定义默认参数要牢记一点：默认参数必须指向不变对象！

# def power2(x, n = 2):
#     s = 1
#     while n > 0:
#         s = s * x
#         n -= 1
#     return s

# print(power2(3, 3))
# print(power2(3))


# 可变参数
#######################################################################################
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# def sum(numbers):
#     sum = 0
#     for n in numbers:
#         sum += n
#     return sum

# print(sum([1,2,3]))

# # Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
# def sum2(*numbers):
#     sum = 0
#     for n in numbers:
#         sum += n
#     return sum

# print(sum2(1,2,3))


# 关键字参数
#######################################################################################
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
# def person(name, age, **kw):
#     print('name is ', name, ',age is ', age, 'other is ', kw)

# person('lisa', 15, gender=1, hobby='read')


# 命名关键字参数
#######################################################################################
# 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
#example A
# def person(name, age, *, gender, job):
#     print(name, age, gender, job)

# person('jon', 15, gender=1, job='singer')

#example B
# def person(name, age, *args, gender, job):
#     print(name, age, args, gender, job)

# person('lisa', 17, 'read', 'swim', gender=1, job='engineer')

#example C
# def person(name, age, *, gender=1, job):
#     print(name, age, gender, job)

# person('lisa', 11, job='engineer')


# 参数组合
#######################################################################################
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
# def fn1(a, b, c=0, *args, **kw):
#     print('a = ', a, ', b = ', b, ', c = ', c, ', args = ', args, ', kw = ', kw)

# fn1(1, 2)                   # a =  1 , b =  2 , c =  0 , args =  () , kw =  {}
# fn1(1,2,3)                  # a =  1 , b =  2 , c =  3 , args =  () , kw =  {}
# fn1(1,2,3,'a','b')          # a =  1 , b =  2 , c =  3 , args =  ('a', 'b') , kw =  {}
# fn1(1,2,3,'a','b',x=99)     # a =  1 , b =  2 , c =  3 , args =  ('a', 'b') , kw =  {'x': 99}


# def fn2(a, b, c=0, *, d, **kw):
#     print('a = ', a, ', b = ', b, ', c = ', c, ', d = ', d, ', kw = ', kw)

# fn2(1,2,d=5,ext=None)       # a =  1 , b =  2 , c =  0 , d =  5 , kw =  {'ext': None}

# # 通过一个tuple和dict，你也可以调用上述函数：
# 要注意定义可变参数和关键字参数的语法：
# *args是可变参数，args接收的是一个tuple；
# **kw是关键字参数，kw接收的是一个dict。

# args = (1,2,3,4)
# kw = {'d': 9, 'x': '#'}
# fn1(*args, **kw)
# # a =  1 , b =  2 , c =  3 , args =  (4,) , kw =  {'d': 9, 'x': '#'}


# args2 = (1,2,3)
# kw2 = {'d': 9, 'x': '#'}
# fn2(*args2, **kw2)
# # a =  1 , b =  2 , c =  3 , d =  9 , kw =  {'x': '#'}



# practice
def product(x, *nums):
    for y in nums:
        x *= y
    return x

print(product(5))
print(product(5,6))