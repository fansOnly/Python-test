# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# hashlib
# 摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）
import hashlib

# MD5
md5 = hashlib.md5()
md5.update('hello, python3 hahahhah'.encode('utf-8'))
print('md5', md5.hexdigest())
# edd84a5fc0110f52322e9015f9171428

md5 = hashlib.md5()
md5.update('hello, python3'.encode('utf-8'))
md5.update(' hahahhah'.encode('utf-8'))
print('md5', md5.hexdigest())
print('*'*100)


# SHA1
# SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。
sha1 = hashlib.sha1()
sha1.update('hello, python3 hahahhah'.encode('utf-8'))
print('sha1', sha1.hexdigest())
print('*'*100)


# practice 根据用户输入的口令，计算出存储在数据库中的MD5口令：
def calc_md5(password):
    # pass
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()

# password = input('请输入你的密码：')
# print(calc_md5(password))

# practice 设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False：
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user, password):
    # pass
    return db[user] == calc_md5(password)

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')
print('*'*100)


# practice 根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5：
import hashlib, random
db = {}

def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')

# print("用户注册开始>>>>>>")
# username = input('请输入用户名：')
# password = input('请输入密码：')
# register(username, password)
# print('注册成功>>>>>>', db)
# print('*'*100)

# 然后，根据修改后的MD5算法实现用户登录的验证：
class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username, password):
    user = db[username]
    return user.password == get_md5(password+user.salt)

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')