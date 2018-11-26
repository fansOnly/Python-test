#!user/bin/env python3
# -*- coding: utf-8 -*-

# python 多重继承 + 拓扑排序
#################################################################################################
# 从DAG途中选择一个没有前驱(即入度为0)的顶点并输出
# 从图中删除该顶点和所有以它为起点的有向边。
# 重复1和2直到当前DAG图为空或当前途中不存在无前驱的顶点为止。后一种情况说明有向图中必然存在环。

class A(object):
    def bar(self):
        print('A bar')
    def foo(self):
        print('A foo')
class B(object):
    def bar(self):
        print('B bar')
    def foo(self):
        print('B foo')
class C1(A,B):
    pass
class C2(A,B):
    def bar(self):
        print('C2 bar')
class D(C1,C2):
    pass

if __name__ == '__main__':
    print(D.__mro__)
    d = D()
    d.bar()
    d.foo()

# 找到入度为0的点，只有一个D，把D拿出来，把D相关的边剪掉
# 现在有两个入度为0的点(C1,C2)，取最左原则，拿C1，剪掉C1相关的边，这时候的排序是{D,C1}
# 现在我们看，入度为0的点(C2),拿C2,剪掉C2相关的边，这时候排序是{D,C1,C2}
# 接着看，入度为0的点(A,B),取最左原则，拿A，剪掉A相关的边，这时候的排序是{D,C1,C2,A}
# 继续，入度哦为0的点只有B，拿B，剪掉B相关的边，最后只剩下object
# 所以最后的排序是{D,C1,C2,A,B,object}


class AA(object):
    def bar(self):
        print('AA bar')
    def foo(self):
        print('AA foo')
class BB(object):
    def bar(self):
        print('BB bar')
    def foo(self):
        print('BB foo')
class CC1(AA):
    pass
class CC2(BB):
    def bar(self):
        print('CC2 bar')
class DD(CC1,CC2):
    pass

if __name__ == '__main__':
    print(DD.__mro__)
    d = DD()
    d.bar()
    d.foo()


# 找到入度为0的顶点，只有一个D，拿D，剪掉D相关的边
# 得到两个入度为0的顶点(C1,C2),根据最左原则，拿C1，剪掉C1相关的边，这时候序列为{D,C1}
# 接着看，入度为0的顶点有两个(A,C1),根据最左原则，拿A，剪掉A相关的边，这时候序列为{D,C1,A}
# 接着看，入度为0的顶点为C2,拿C2，剪掉C2相关的边，这时候序列为{D,C1,A,C2}
# 继续，入度为0的顶点为B，拿B，剪掉B相关的边，最后还有一个object
# 所以最后的序列为{D,C1,A,C2,B,object}