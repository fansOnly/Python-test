# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# Socket
import socket

# 客户端
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 参数是一个tuple，包含地址和端口号。
# 80端口是Web服务的标准端口。其他服务都有对应的标准端口号，例如SMTP服务是25端口，FTP服务是21端口，等等。端口号小于1024的是Internet标准服务的端口，端口号大于1024的，可以任意使用。
s.connect(('www.sina.com.cn', 80))

# TCP连接创建的是双向通道，双方都可以同时给对方发数据。但是谁先发谁后发，怎么协调，要根据具体的协议来决定。
# HTTP协议规定客户端必须先发请求给服务器，服务器收到后才发数据给客户端。
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接收数据时，调用recv(max)方法，一次最多接收指定的字节数，因此，在一个while循环中反复接收，直到recv()返回空数据，表示接收完毕，退出循环。
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
    
data = b''.join(buffer)

# 当我们接收完数据后，调用close()方法关闭Socket，这样，一次完整的网络通信就结束了：
s.close()

# 接收到的数据包括HTTP头和网页本身，我们只需要把HTTP头和网页分离一下，把HTTP头打印出来，网页内容保存到文件：
header, html = data.split(b'\r\n\r\n', 1)
print('header', header.decode('utf-8'))
# # 把接收的数据写入文件:
with open('F:\python\Python-test\learning\网络编程\TCP编程\sina.html', 'wb') as f:
    f.write(html)