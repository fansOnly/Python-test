# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# sorted
#######################################################################################################
# 排序算法
# 排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。如果是数字，我们可以直接比较，但如果是字符串或者两个dict呢？直接比较数学上的大小是没有意义的，因此，比较的过程必须通过函数抽象出来。

# s1 = sorted([1,4,-2,-50,1000,400])
# print(s1)

# s2 = sorted([1,4,-2,-50,1000,400], key=abs)
# print(s2)

# 默认情况下，对字符串排序，是按照ASCII的大小比较的
# s3 = sorted(['bob', 'about', 'Zoo', 'Credit'])
# print(s3)

# s4 = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
# print(s4)

# practice 1
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    # pass
    return t[0].lower()

L2 = sorted(L, key=by_name)
print("按名字排序\n",L2)

def by_score(t):
    # pass
    return -t[1]

L3 = sorted(L, key=by_score)
print("按成绩从高到低排序\n",L3)