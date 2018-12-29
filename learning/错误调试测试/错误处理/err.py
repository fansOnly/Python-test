#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# 错误、调试和测试
##############################################################################################

# 错误处理
##############################################################################################
# try  ... except ... finally...
# try:
#     print('try...')
#     r = 10 / 0
#     print('result: ', r)
# except ZeroDivisionError as e:
#     print('except: ', e)
# else:
#     print('no error!')
# finally:
#     print('finally...')



# 调用栈
# 如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出
# def foo(s):
#     return 10/ int(s)
# def bar(s):
#     return foo(s) * 2
# def main():
#     bar('0')
# main()


# 记录错误
# Python内置的logging模块可以非常容易地记录错误信息：
# import logging
# def foo(s):
#     return 10 / int(s)
# def bar(s):
#     return foo(s) * 2
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)
# main()
# print('END')

# 抛出错误
# class FooError(ValueError):
#     pass
# def foo(s):
#     n = int(s)
#     if n == 0:
#         raise FooError('invalid value %s' % n)
#     return 10 / n
# foo('0')


# 练习
from functools import reduce

def str2num(s):
    if '.' in s:
        return float(s)
    else:
        return int(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    try:
        r1 = calc('100 + 200 + 345')
        print('100 + 200 + 345 = ', r1)
        r2 = calc('99 + 88 + 7.6')
        print('99 + 88 + 7.6 = ', r2)
    except ValueError as e:
        print('error: ', e)
main()