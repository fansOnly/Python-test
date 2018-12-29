# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 正则表达式
# 正则表达式是一种用来匹配字符串的强有力的武器。它的设计思想是用一种描述性的语言来给字符串定义一个规则，凡是符合规则的字符串，我们就认为它“匹配”了，否则，该字符串就是不合法的。


# 进阶

# [0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线；

# [0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等；

# [a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量；

# [a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）。

# ^表示行的开头，^\d表示必须以数字开头。

# $表示行的结束，\d$表示必须以数字结束。


####################################################################################################
# re模块
# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None

import re

r1 = re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
print(r1)
print('*'*100)


# 切分字符串
# 用正则表达式切分字符串比用固定的字符更灵活

str1 = 'a b   c'
print('s1', str1.split(' '))
print('s2', re.split(r'\s+', str1))
str2 = 'a , b,   c'
print('s3', re.split(r'[\s\,]+', str2))
str3 = 'a, b, ;;   c'
print('s3', re.split(r'[\s\,\;]+', str3))
print('*'*100)


# 分组
# 除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group）

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m, m.groups())
print('*'*100)


# 贪婪匹配
# 正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符
# 加个?就可以让\d+采用非贪婪匹配

m2 = re.match(r'^(\d+)(0*)$', '102300')
print(m2.groups())
m3 = re.match(r'(\d+?)(0*)$', '102300')
print(m3.groups())
print('*'*100)


# 编译
# 当我们在Python中使用正则表达式时，re模块内部会干两件事情：
# a.编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
# b.用编译后的正则表达式去匹配字符串。

re_phone = re.compile(r'(\d{3})-(\d{3,8})')
s1 = re_phone.match('010-225600')
s2 = re_phone.match('010-1524')
print(s1.groups())
print(s2.groups())
print('*'*100)


# practise 1
# 请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：
# someone@gmail.com
# bill.gates@microsoft.com

def is_valid_email(addr):
    re_email = re.compile(r'^([\w\.]*)\@(\w+)\.(com|cn|org)$')
    if re_email.match(addr):
        return True
    else:
        return False

assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')
print('*'*100)


# practise 2 - 提取出带名字的Email地址：
def name_of_email(addr):
    re_email = re.compile(r'^\<?([\w\s]*)?\>?\s?([\w]*)\@(\w+)\.(com|cn|org)$')
    res = re_email.match(addr)
    if res:
        return res.group(1)
    else:
        return None

assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
print('*'*100)