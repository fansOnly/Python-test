# !/usr/bin/env python3
# -*- coding: utf-8 -*-

##########################################################################################
# StringIO - 在内存中读写str
# getvalue()方法用于获得写入后的str。

# 要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可：
from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue())

# 要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：
f = StringIO('hello\nworld!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
print('*'*100)

# BytesIO
# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.tell(),f.getvalue())

# 读取
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.tell(),f.read())
print('*'*100)


# tell 方法获取当前文件读取指针的位置
# seek 方法，用于移动文件读写指针到指定位置,有两个参数，第一个offset: 偏移量，需要向前或向后的字节数，正为向后，负为向前；第二个whence: 可选值，默认为0，表示文件开头，1表示相对于当前的位置，2表示文件末尾
# 用seek方法时，需注意，如果你打开的文件没有用'b'的方式打开，则offset无法使用负值
f = StringIO('adadasd')
print(f.tell())
print(f.getvalue())
f.write('1312')
print(f.tell())
print(f.getvalue())
f.seek(2)
print(f.tell())
f.write('x')
print(f.getvalue())
f.seek(0,2)
print(f.tell())
f.write('yyyyy')
print(f.getvalue())
print('*'*100)