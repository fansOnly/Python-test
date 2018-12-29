# !/usr/bin/env python3
#  -*- coding: utf-8 -*-

# 装饰器
# 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
# 本质上，decorator就是一个返回函数的高阶函数
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print("call %s()" % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    pass

now()
print(now.__name__)
print('********************************************')

def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s:call %s()' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log2('打印日期')
def now2():
    pass

now2()
print(now2.__name__)
print('********************************************')

# practice 1 通用装饰器
def log3(*args):
    text = ''
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('func start')
            print('%scall %s()' % (text, func.__name__))
            res = func(*args, **kw)
            print('func end')
            return res
        return wrapper
    if len(args) == 1:
        if callable(args[0]):
            return decorator(args[0])
        else:
            text = args[0]
            return decorator
    else:
        return decorator

# @log3
# @log3()
@log3('打印日志：')
def test():
    pass

test()
print('********************************************')

# practice 2 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
import time, functools
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        t1 = time.time()
        res = fn(*args, **kw)
        t2 = time.time()
        print('%s executed in %s ms' % (fn.__name__, t2 - t1))
        return res
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')