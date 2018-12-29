# !/usr/bin/env python3
# -*-* coding: utf-8 -*-

# collections

##################################################################################
# namedtuple
# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1,2)
print(p.x, p.y)
print(isinstance(p, Point), isinstance(p, tuple))
print('*'*100)


##################################################################################
# deque
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
from collections import deque

p = deque(['a', 'b', 'c', 'd'])
p.append('e')
print(p)
p.appendleft('x')
print(p)
print('*'*100)


##################################################################################
# defaultdict
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
from collections import defaultdict
s = defaultdict(lambda: 'N/A')
s['key1'] = 'abc'
print(s['key1'], s['key2'])
print('*'*100)


##################################################################################
# OrderedDict
# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
# 如果要保持Key的顺序，可以用OrderedDict：
# OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
from collections import OrderedDict

d1 = dict([('a', 1), ('b', 2), ('c', 3)])
print('dict', d1)
d2 = OrderedDict([('a', 1), ('c', 3), ('b', 2)])
print('OrderedDict', d2)
d3 = OrderedDict()
d3['a'] = 1
d3['v'] = 3
d3['b'] = 5
print('OrderedDict', d3)
print('*'*100)

# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
class LastUpdateOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdateOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set', (key, value))
        else:
            print('add', (key, value))
        OrderedDict.__setitem__(self, key, value)

if __name__=='__main__':
    od = LastUpdateOrderedDict(3)
    od[1] = 'a'
    od[2] = 'b'
    od[3] = 'c'
    od[4] = 'd'
    od[3] = 'cc'
    print('od', od)
print('*'*100)

##################################################################################
# ChainMap
# 应用程序往往都需要传入参数，参数可以通过命令行传入，可以通过环境变量传入，还可以有默认参数。我们可以用ChainMap实现参数的优先级查找，即先查命令行参数，如果没有传入，再查环境变量，如果没有，就使用默认参数。

from collections import ChainMap
import os, argparse

# 构造缺省参数:
defaults = {
    'color': 'red',
    'user': 'guest'
}

# 构造命令行参数:
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = { k: v for k, v in vars(namespace).items() if v }

# 组合成ChainMap:
combined = ChainMap(command_line_args, os.environ, defaults)

# 打印参数:
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])
print('*'*100)



##################################################################################
# Counter
from collections import Counter

c = Counter()
for ch in 'programmer':
    c[ch] = c[ch] + 1

print('count', c)
print('*'*100)