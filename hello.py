#!user/bin/env python3
# -*- coding: utf-8 -*-

# name = input('please input your name:')
# print("name", name)


# a = 100
# if a > 0:
#     print(a)
# else:
#     print(-a)


# print('I\'m \"ok\"! ')
# print('\\\n\/\t\\')
# print(r'\\\n\/\t\\')
# print('''line1
# line2
# line3''')
# print(r'''line1
# line2
# line3''')

# print(None)

# print('''n = 123
# f = 456.789
# s1 = 'Hello, world'
# s2 = 'Hello, \\\'Adam\\\''
# s3 = r'Hello, "Bart"'
# s4 = r'\'\'Hello,\nLisa!'\'\'
# ''')

# print('阿达')
# print(len('扎三级的'))
# print(len('这是你是'.encode('utf-8')))


# print('%.2f' % (1.457839))
# print('%2d - %02d' % (1, 5))
# print('%2d - %02d' % (1, 15))
# print('%.1f%s' % ((85 - 72) / 72 * 100, '%'))
# print('%.1f%%' % ((85 - 72) / 72 * 100))


# BMI = 80.5 / 1.75**2
# print(BMI)
# if BMI < 18.5:
#     print('过轻')
# elif BMI >= 18.5 and BMI <= 25:
#     print('正常')
# elif BMI >25 and BMI < 28:
#     print('过重')
# elif BMI >= 28 and BMI <= 32:
#     print('肥胖')
# else:
#     print('过度肥胖')

# sum = 0
# for x in range(101):
#     sum += x
# print(sum)

# sum = 0
# n = 99
# while n > 0:
#     n = n - 2
#     sum += n
# print(sum)

# print('地址邮编')
# adict = dict(北京='111111', 上海='222222', 深圳='333333')
# while True:
    
#     print('请输入地址名：')
#     address = input()
#     if address in adict.keys():
#         print(address, ':', adict.get(address))
#     else:
#         print('没有这个地址，请输入邮编：')
#         adZipid = input()
#         adict.update({address: adZipid})


import math


def quadratic(a,b,c):
    delta = b**2 - 4*a*c
    m = math.sqrt(delta)
    x1 = (m - b) /a/2
    x2 = (- m - b) /a/2
    return x1, x2


print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))
