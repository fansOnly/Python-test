# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 操作文件和目录
# Python内置的os模块也可以直接调用操作系统提供的接口函数
# os模块的某些函数是跟操作系统相关的。

import os
print('操作系统类型',os.name)
# print(os.uname())  # 
print('环境变量', os.environ)
print('语言', os.environ.get('LANG'))
print('*'*100)

###########################################################################################################
# 操作文件和目录
# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：
print('当前文件绝对路径', os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
path = os.path.join(os.path.abspath('.'), 'ss')
print(path)
os.mkdir(path)
os.rmdir(path)
print('*'*100)
# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符
# 在Linux/Unix/Mac下，os.path.join()返回这样的字符串：part-1/part-2
# 而Windows下会返回这样的字符串：part-1/part-2

# 通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
path = 'IO编程/操作文件和目录/hello.txt'
print(os.path.split(path))
print('扩展名', os.path.splitext(path))

# *********************************************************************************************
with open('IO编程/操作文件和目录/rename.txt', 'w') as f:
    f.write('rename self')
# 文件重命名
os.rename('IO编程/操作文件和目录/rename.txt', 'IO编程/操作文件和目录/rename.py')
# 删除文件
os.remove('IO编程/操作文件和目录/rename.py')
print('*'*100)


# *********************************************************************************************
# shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。
# 复制文件
import shutil
shutil.copyfile('IO编程/操作文件和目录/hello.txt', 'IO编程/操作文件和目录/hello_copy.txt')

f1 = open('IO编程/操作文件和目录/hello.txt', 'r')
f2 = open('IO编程/操作文件和目录/none.txt', 'w')
shutil.copyfileobj(f1, f2)

# ******************************************************************************************
# 列出当前目录下的所有目录
print([x for x in os.listdir('.') if os.path.isdir(x)])
# 列出当前目录下的所有.py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext('x')[1] == '.txt'])
print('*'*100)

# practice 1 利用os模块编写一个能实现dir -l输出的程序。
import os, time
dirpath = '.'

# 把二进制字符转换成权限码
def str2word(numstr):
    wordstr = ''
    words = ['r','w','x']
    for i, x in enumerate(numstr):
        if x == '1':
            wordstr += (lambda i,words : words[ i % 3])(i,words)
        else:
            wordstr += '-'
    return wordstr

def listFile():
    for x in os.listdir(dirpath):
        if os.path.isdir(x):
            path = os.path.join(dirpath, x)
            stat = os.stat(path)
            num = [0]
            for y in os.listdir(path):
                num[0] +=1
            print(str2word(str((bin(stat.st_mode)[-9:]))), end='\t')
            print(num[0], end='\t')
            print(stat.st_uid, end='\t')
            print(stat.st_gid, end='\t')
            mtime = time.localtime(stat.st_mtime)
            print(mtime.tm_mon, end='\t')
            print(mtime.tm_mday, end='\t')
            print(str(mtime.tm_hour)+':'+str(mtime.tm_min), end='\t')
            print(stat.st_size, end='\t')
            print(x)

print('权限\t        文件数\t用户id\t群组id\t月份\t日期\t时间\t大小\t文件夹')
listFile()


# practice 2 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
dirpath = '.'
absfiles = []
def searchFile(name, path):
    # pass
    for x in os.listdir(path):
        path1 = os.path.abspath(path)
        apath = os.path.join(path1, x)
        
        if os.path.isfile(apath) and os.path.splitext(apath)[0].find(name) != -1:
            absfiles.append(apath)
        else:
            if os.path.isdir(apath):
                searchFile(name, apath)

searchFile('hello', dirpath)
print('绝对路径:', [x for x in absfiles])