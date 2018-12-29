# !/usr/bin/env phthon3
# -*- coding: utf-8 -*-


# struct
# 解决bytes和其他二进制数据类型的转换。

import struct

# pack的第一个参数是处理指令，'>I'的意思是：
# >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
# 后面的参数个数要和处理指令一致。
s1 = struct.pack('>I', 10240099)
print('', s1)

# 根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。
s2 = struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
print('', s2)
print('*'*100)


# Windows的位图文件（.bmp）是一种非常简单的文件格式，我们来用struct分析一下。
# 两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；
# 一个4字节整数：表示位图大小；
# 一个4字节整数：保留位，始终为0；
# 一个4字节整数：实际图像的偏移量；
# 一个4字节整数：Header的字节数；
# 一个4字节整数：图像宽度；
# 一个4字节整数：图像高度；
# 一个2字节整数：始终为1；
# 一个2字节整数：颜色数。
s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
print(struct.unpack('<ccIIIIIIHH', s))
print('*'*100)



# practice 检查任意文件是否是位图文件，如果是，打印出图片大小和颜色数。
import base64, struct

bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAAAAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/AHwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHwAfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')

def bmp_info(data):
    bmp_data = struct.unpack('<ccIIIIIIHH', data[:30])
    if bmp_data[0] == b'B' and (bmp_data[1] == b'M' or bmp_data[1] == b'A'):
        return {
            'width': bmp_data[6],
            'height': bmp_data[7],
            'color': bmp_data[9]
        }
    else:
        print('this is not a bmp')

bi = bmp_info(bmp_data)
assert bi['width'] == 28
assert bi['height'] == 10
assert bi['color'] == 16
print('ok')

with open(r'F:\python\Python-test\learning\常用内建模块\files\0.jpg','rb') as f:
    bmp_data2 = f.read()
bi2 = bmp_info(bmp_data2)
print("bi2", bi2)

with open(r'F:\python\Python-test\learning\常用内建模块\files\1.bmp', 'rb') as f:
    bmp_data3 = f.read()
bi3 = bmp_info(bmp_data3)
print("bi3", bi3)