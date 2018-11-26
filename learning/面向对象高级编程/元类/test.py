#use/bin/env python3
#-*- coding: utf-8 -*-

# 使用元类
######################################################################################

# type()
# type()函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello。
# class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。
# 要创建一个class对象，type()函数依次传入3个参数：
# 1/class的名称；
# 2/继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# 3/class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

# def fn(self, name='snow'):
#     print('hello %s' % name)
# H = type('Hello', (object,), dict(hello=fn))
# h = H()
# h.hello()
# print(H.__name__)
# print(type(H))
# print(type(h))


######################################################################################
# metaclass 元类
# 先定义metaclass，就可以创建类，最后创建实例。
# 按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass：

# __new__()方法接收到的参数依次是：
# 1/当前准备创建的类的对象；
# 2/类的名字；
# 3/类继承的父类集合；
# 4/类的方法集合。
# class ListMetaclass(type):
#     def __new__(cls, name, bases, attrs):
#         attrs['add'] = lambda self, value: self.append(value)
#         return type.__new__(cls, name, bases, attrs)
# class MyList(list, metaclass=ListMetaclass):
#     pass
# L1 = MyList()
# print(L1)
# L1.add(1)
# print(L1)

# L2 = list()
# L2.add(2)


######################################################################################
# ORM框架
# ORM全称“Object Relational Mapping”，即对象-关系映射，就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句。

class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)
# x1 = Field('namex', 'vachar(100)')
# print(x1)
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'vachar(100)')
# x2 = StringField('x2')
# print(x2)
class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'int(11)')

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mappings: %s => %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        # print(attrs)
        return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise KeyError('Model can`t find attribute %s' % key)
    def __setattr__(self, key, value):
        self[key] = value
    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append(str(getattr(self, k, None)))
            args.append(getattr(self,k,None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % args)

class User(Model):
    id = IntegerField('userid')
    name = StringField('username')
    age = IntegerField('userage')
    gender = StringField('usergender')
x3 = User(id= 1, name='bug', age=15, gender='male')
x3.save()

