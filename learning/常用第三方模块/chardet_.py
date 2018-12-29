# !/usr/bin/env python3
# -*- coding: utf-8 -*-


# chardet
# 检测出的编码是ascii，注意到还有个confidence字段，表示检测的概率是1.0（即100%）。
import chardet

print(chardet.detect(b'Hello, world!'))
print('*'*100)


# 检测GBK编码的中文：
data = '离离原上草，一岁一枯荣'.encode('gbk')
print(chardet.detect(data))
print('*'*100)


# 对UTF-8编码进行检测：
data = '离离原上草，一岁一枯荣'.encode('utf-8')
print(chardet.detect(data))
print('*'*100)


# 对日文进行检测：
data = '最新の主要ニュース'.encode('euc-jp')
print(chardet.detect(data))
print('*'*100)