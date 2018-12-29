# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口
s.bind(('127.0.0.1', 9999))

# 创建Socket时，SOCK_DGRAM指定了这个Socket的类型是UDP。绑定端口和TCP一样，但是不需要调用listen()方法，而是直接接收来自任何客户端的数据：
# recvfrom()方法返回数据和客户端的地址与端口，这样，服务器收到数据后，直接调用sendto()就可以把数据用UDP发给客户端。
print('bind UDP to 127.0.0.1:9999')
while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)
    print('received from %s:%s' % addr)
    s.sendto(b'hello, %s' % data, addr)