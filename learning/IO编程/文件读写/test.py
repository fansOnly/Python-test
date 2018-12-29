# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 文件读写
# 在磁盘上读写文件的功能都是由操作系统提供的，现代操作系统不允许普通的程序直接操作磁盘，所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），或者把数据写入这个文件对象（写文件）。

##############################################################################################
# 读文件
# 要以读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标示符：

# f1 = open('hello.txt', 'r')
# c1 = f1.read()
# print(c1)
# f1.close()

# try:
#     f = open('hello.txt', 'r')
#     c1 = f.read()
#     print(c1)
# finally:
#     if f:
#         f.close()

with open('IO编程/文件读写/hello.txt', 'r') as f:
    print(f.read())
print('*'*100)
    
# 如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：
# with open('IO编程/文件读写/long.txt', 'r') as f:
#     for line in f.readlines():
#         print(line.strip())

# *********************************************************************************************
# file-like Object
# 像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。除了file外，还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行。

# StringIO就是在内存中创建的file-like Object，常用作临时缓冲。
# *********************************************************************************************


##############################################################################################
# 二进制文件
# 前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：
with open('IO编程/文件读写/0.jpg', 'rb') as f:
    print(f.read())
print('*'*100)

##############################################################################################
# 字符编码
# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：
with open('IO编程/文件读写/gbk.txt', 'r', encoding='gbk') as f:
    print(f.read())
print('*'*100)

##############################################################################################
# UnicodeDecodeError
with open('IO编程/文件读写/error.txt', 'r', encoding='gbk', errors='ignore') as f:
    print(f.read())
print('*'*100)

###############################################################################################
# 写文件  w, wb, a(追加修改)
with open('IO编程/文件读写/123.txt', 'w') as f:
    f.write('hehe')
with open('IO编程/文件读写/123.txt', 'w') as f:
    f.write('haha')
with open('IO编程/文件读写/123.txt', 'a') as f:
    f.write('hihi')
with open('IO编程/文件读写/123.txt', 'r') as f:
    print(f.read())
print('*'*100)


# practice 1
fpath = r'C:\Windows\system.ini'

with open(fpath, 'r') as f:
    s = f.read()
    print(s)
print('*'*100)