# !/usr/bin/env python3
# -*- coding: utf-8 -*-


############################################################################################
# map/reduce

# def f(x):
#     return x*x

# r = map(f, [1,2,3,4])
# print(list(r))

# from functools import reduce
# def add(x, y):
#     return x + y
# s = reduce(add,[1,2,3,4])
# print(s)

# def add2(x, y):
#     return x*10 + y
# s2 = reduce(add2, [1,2,3,4])
# print(s2)


# from functools import reduce
# def add2(x, y):
#     return x*10 + y
# def char2num(s):
#     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#     return digits[s]
# s3 = reduce(add2, map(char2num, '12345'))
# print(s3)

# from functools import reduce
# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# def str2int(s):
#     def add2(x, y):
#         return x*10 + y
#     def char2num(i):
#         return DIGITS[i]
#     return reduce(add2, map(char2num, s))

# s4 = str2int('353453')
# print(s4)

# practice 1
# def normalize(name):
#     # pass
#     return name[0].upper() + name[1:].lower()

# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)

# practice 2
# def prod(L):
#     # pass
#     return reduce(lambda x, y: x*y, L)

# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')

# practice 3
# from functools import reduce
# def str2float(s):
#     # pass
#     s1 = reduce(lambda x, y: x * 10 + y, map(int, s.split('.')[0]))
#     s2 = reduce(lambda x, y: x * 10 + y, map(int, s.split('.')[1]))
#     print(s1, s2)
#     return s1 + s2/(10**len(str(s2)))

# print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#     print('测试成功!')
# else:
#     print('测试失败!')