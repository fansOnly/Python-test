# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 函数作为返回值
# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum

f1 = lazy_sum(1,2,3,4,5)
f2 = lazy_sum(1,2,3,4,5)
s1 = f1()
s2 = f2()
print(s1, s2, f1 == f2)

# 闭包（Closure）
# *********************************************************************
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f())
    return fs

f1, f2, f3 = count()

# print(f1(), f2(), f3())
print(f1, f2, f3)

# practice 1 利用闭包返回一个计数器函数，每次调用它返回递增整数：
# ？函数内部实际上是不允许直接修改全局变量的引用
# def createCounter():
#     i = [0]
#     def counter():
#         i[0] += 1
#         return i[0]
#     return counter

def createCounter():
    def counter():
        n = 1
        while True:
            yield n
            n +=1
    c = counter()
    def g():
        return next(c)
    return g

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')