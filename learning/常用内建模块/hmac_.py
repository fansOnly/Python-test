# !/use/bin/env python3
# -*- coding: utf-8 -*-

# hmac Keyed-Hashing for Message Authentication
# 它通过一个标准算法，在计算哈希的过程中，把key混入计算过程中。
import hmac

password = b'Hello, world!'
key = b'secret'
h1 = hmac.new(key, password, digestmod='MD5')
print('hmac', h1.hexdigest())
print('*'*100)


# practice
import hmac, random

def hmac_md5(key, password):
    return hmac.new(key.encode('utf-8'), password.encode('utf-8'), digestmod='MD5').hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac_md5(self.key, password)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username, password):
    user = db[username]
    return user.password == hmac_md5(user.key, password)

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')