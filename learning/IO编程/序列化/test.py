# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 序列化
###############################################################################################
# 变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等
# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
# 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
# Python提供了pickle模块来实现序列化。

# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
import pickle
dirpath = 'F:\python\Python-test\learning\IO编程\序列化\\'

d = dict(name='Bob', age=15)
json = pickle.dumps(d)
print(json)

f = open(dirpath +'pick.txt', 'wb')
pickle.dump(d, f)
f.close()

# 当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象


f = open(dirpath + 'pick.txt', 'rb')
d2 = pickle.load(f)
print(d2)
print('*'*100)


# JSON
# JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：
# JSON类型	     Python类型
# {}	        dict
# []	        list
# "string"	    str
# 1234.56	    int或float
# true/false	True/False
# null	        None
# Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。我们先看看如何把Python对象变成一个JSON
# 由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str与JSON的字符串之间转换。
import json
d = dict(name='Bob', age=15)
json_str = json.dumps(d)
print("json序列化对象:", json_str)
json_str2 = json.loads(json_str)
print('json反序列化', json_str2)
print('*'*100)


# JSON进阶
# Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化：
class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

def stu2dict(std):
    return {
        'name': std.name,
        'age': std.age
    }
s = Student('Bob',15)
json_s = json.dumps(s, default = stu2dict)
print('class2json', json_s)

# 因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。
print('class2json', json.dumps(s, default = lambda obj: obj.__dict__))
# 如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例：
def dict2stu(d):
    return Student(d['name'],d['age'])
json_str = '{"age": 20, "name": "Bob"}'
print('json2class',json.loads(json_str, object_hook=dict2stu))
print('*'*100)


# practice 1 对中文进行JSON序列化时，json.dumps()提供了一个ensure_ascii参数，观察该参数对结果的影响：
d = dict(name='小明', age=20)
json_d = json.dumps(d, ensure_ascii = True)
json_d2 = json.dumps(d, ensure_ascii = False)
print(json_d)
print(json_d2)
print('*'*100)