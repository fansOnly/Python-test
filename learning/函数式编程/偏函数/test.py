# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 偏函数
# functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单
import functools
# kw = { 'base': 2 }
# int('10010', **kw)
int2 = functools.partial(int, base=2)
s1 = int2('10000000')
print(s1)


# 创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数
# *args 在左，**kw在右