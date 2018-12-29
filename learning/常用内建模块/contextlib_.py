# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# contextlib
# 在Python中，读写文件这样的资源要特别注意，必须在使用完毕后正确关闭它们
# 并不是只有open()函数返回的fp对象才能使用with语句。实际上，任何对象，只要正确实现了上下文管理，就可以用于with语句。

# 实现上下文管理是通过__enter__和__exit__这两个方法实现的

class Query(object):
    def __init__(self, name):
        self.name = name
    
    def __enter__(self):
        print('begin...')
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('error')
        else:
            print('end...')
    
    def query(self):
        print('Query info about %s' % self.name)

with Query('Bob') as f:
    f.query()


######################################################################################
# @contextmanager
from contextlib import contextmanager

class Query2(object):
    def __init__(self, name):
        self.name = name
    
    def query(self):
        print('Query2 info about %s' % self.name)
print('*'*100)

@contextmanager
def query2(name):
    print('begin...')
    q = Query2(name)
    yield q
    print('end...')

with query2('Bob2') as f:
    f.query()
print('*'*100)

# 很多时候，我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现
@contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('</%s>' % name)

with tag('h1') as f:
    print("hello")
    print('world')
print("*"*100)


########################################################################################
# @closing
# 可以用closing()来把对象变为上下文对象。
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)

# @contextmanager
# def closing(thing):
#     try:
#         yield thing
#     finally:
#         thing.close()