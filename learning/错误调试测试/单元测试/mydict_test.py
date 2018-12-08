#!usr/bin/env python3
#-*- coding: utf-8 -*-

# 为了编写单元测试，我们需要引入Python自带的unittest模块
# 编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承。
# 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。

# assertEqual()  断言函数返回的结果与目标值相等
# 抛出指定类型的Error，比如通过d['empty']访问不存在的key时，断言会抛出KeyError：
# with self.assertRaises(KeyError):
    # value = d['empty']
# 通过d.empty访问不存在的key时，我们期待抛出AttributeError：
# with self.assertRaises(AttributeError):
    # value = d.empty

# 1/unittest.main()
# 2/在命令行通过参数-m unittest直接运行单元测试：

import unittest

from mydict import Dict

class TestDict(unittest.TestCase):
    def setUp(self):
        print('setup...')

    def test_init(self):
        d = Dict(a=1,b='test')
        self.assertEqual(d.a , 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')
    
    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

    def tearDown(self):
        print('tearDown...')


if __name__ == '__main__':
    unittest.main()