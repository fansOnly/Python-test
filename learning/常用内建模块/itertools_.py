# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# itertools
# itertools提供了非常有用的用于操作迭代对象的函数。
import itertools

#########################################################################################
# count()会创建一个无限的迭代器
# natuals = itertools.count(1)
# for n in natuals:
#     if n < 5:
#         print(n)
# print('*'*100)


#########################################################################################
# cycle()会把传入的一个序列无限重复下去：
# cycles = itertools.cycle('ABC')
# i = 1
# for c in cycles:
#     if i < 5:
#         print(c)
#     i += 1
# print('*'*100)


#########################################################################################
# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
ns = itertools.repeat('X', 5)
for x in ns:
    print(x)
print('*'*100)


#########################################################################################
# 无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：
natualsx = itertools.count(1)
ns = itertools.takewhile(lambda x: x<=5, natualsx)
print(list(ns))
print('*'*100)


#########################################################################################
# chain()
# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
for c in itertools.chain('ABC', 'XYZ'):
    print(c)
print('*'*100)


#########################################################################################
# groupby()
# groupby()把迭代器中相邻的重复元素挑出来放在一起：
for key, group in itertools.groupby('AAaaBbbCCcc'):
    print(key, list(group))
print('*'*100)

for key, group in itertools.groupby('AAaaBbbCCcc', lambda c: c.upper()):
    print(key, list(group))
print('*'*100)


# practice   计算圆周率可以根据公式：
# 利用Python提供的itertools模块，我们来计算这个序列的前N项和：
def pi(N):
    # ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    natuals = itertools.count(1,2)

    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    odds = itertools.takewhile(lambda x: x <= 2*N-1, natuals)
    # print(list(odds))

    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    it = itertools.cycle([4, -4])
    nums = list(map(lambda x: next(it)/x, list(odds)))
    # print(list(nums))

    # step 4: 求和:
    return sum(nums)
    # return reduce(lambda x, y: x + y, nums)

# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')
print('*'*100)