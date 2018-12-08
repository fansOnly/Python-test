# !usr/bin/env python3
# -*- coding: utf-8 -*-

# ###################################################################################
# filter
# Python内建的filter()函数用于过滤序列。
# 和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

# example 1
# def is_odd(x):
#     return x % 2 == 1

# s1 = list(filter(is_odd, [1,2,3,4,5,6,7]))
# print(s1)

# example 2
# def not_empty(s):
#     return s and s.strip()

# s2 = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
# print(s2)


# example 3 用filter求素数
# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n

# def filter_iter(n):
#     return lambda x: x % n > 0

# def primes():
#     yield 2
#     it = _odd_iter()
#     while True:
#         n = next(it)
#         yield n
#         it = filter(filter_iter(n), it)

# for n in primes():
#     if n < 100:
#         print(n)

# practice 1
def is_palindrome(n):
    # pass
    # print(n, "".join(list(str(n))[::-1]), n == int("".join(list(str(n))[::-1])))
    return n == int("".join(list(str(n))[::-1]))

output = filter(is_palindrome, range(1, 10))
print('1~10:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')