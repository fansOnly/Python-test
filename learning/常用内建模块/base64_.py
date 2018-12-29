# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# base64
# 准备一个包含64个字符的数组：['A', 'B', 'C', ... 'a', 'b', 'c', ... '0', '1', ... '+', '/']
# 然后，对二进制数据进行处理，每3个字节一组，一共是3x8=24bit，划为4组，每组正好6个bit：
# 这样我们得到4个数字作为索引，然后查表，获得相应的4个字符，就是编码后的字符串。

# 所以，Base64编码会把3字节的二进制数据编码为4字节的文本数据，长度增加33%，好处是编码后的文本数据可以在邮件正文、网页等直接显示。

# 如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节怎么办？Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉。

import base64

print("常规编码",base64.b64encode(b'binary\x00string'))
print("常规解码",base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))


# 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：
str1 = b'i\xb7\x1d\xfb\xef\xff'
print('常规编码', base64.b64encode(str1))
print('url编码', base64.urlsafe_b64encode(str1))
print('url解码', base64.urlsafe_b64decode('abcd--__'))
print('*'*100)



# practice 1 请写一个能处理去掉=的base64解码函数：
def safe_base64_decode(s):
    # pass
    return base64.b64decode(s+ b'==')
    # return base64.b64decode(s+ b'===='[:len(s)%4])

# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
assert b'abcd' == safe_base64_decode(b'YWJjZA==='), safe_base64_decode('YWJjZA===')
assert b'abcd' == safe_base64_decode(b'YWJjZA===='), safe_base64_decode('YWJjZA====')
print('ok')