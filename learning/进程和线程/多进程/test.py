# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 多进程 - multiprocessing

# Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
# 子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。
# Python的os模块封装了常见的系统调用，其中就包括fork，可以在Python程序中轻松创建子进程：

###################################################################################################
# import os

# print('process %s start...' % os.getpid())
# Only works on Unix/Linux/Mac:
# pid = os.fork()
# if pid == 0:
#     # pass
#     print('I am a child process(%s) and my parent process is %s' % (os.getpid(), os.getppid()))
# else:
#     # pass
#     print('I(%s) just created a process(%s)' % (os.getpid(), pid))
# print('*'*100)

###################################################################################################
# multiprocessing
# multiprocessing模块提供了一个Process类来代表一个进程对象，下面的例子演示了启动一个子进程并等待其结束：
# 1/创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动
# 2/join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。

# from multiprocessing import Process

# def run_pro(name):
#     print('Runing child process %s %s' % (name, os.getpid()))

# if __name__=='__main__':
#     print('Parent process (%s)' % os.getpid())
#     p = Process(target=run_pro, args=('test',))
#     print('process(%s) start...' % os.getpid())
#     p.start()
#     p.join()
#     print('process(%s) end...' % os.getpid())


###################################################################################################
# Pool
# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
# 请注意输出的结果，task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行，这是因为Pool的默认大小在我的电脑上是4，因此，最多同时执行4个进程。这是Pool有意设计的限制，并不是操作系统的限制。

# from multiprocessing import Pool
# import os, time, random

# def long_time_tack(name):
#     print('Run task %s(%s) ...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %.2f' % (name, (end - start)))

# if __name__ == "__main__":
#     # pass
#     print('Parent process %s' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_tack, args=(i,))
#     print('waiting for all subprocesses down')
#     p.close()
#     p.join()
#     print('All subprocesses is down...')

###################################################################################################
# 子进程
# 很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。
# subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup','www.python.org'])
print('Exit code', r)
print('*'*100)


###################################################################################################
# 进程间通信
# Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
from multiprocessing import Process, Queue
import os, time, random

def write(q):
    print('Process to write %s' % os.getpid())
    for value in ['1','2','3','4']:
        print('puts %s to queue' % value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('Process to read %s' % os.getpid())
    while True:
        value = q.get(True)
        print('get %s from queue' % value)

if __name__ == "__main__":
    # pass
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read,args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()


# 总结
# 在Unix/Linux下，可以使用fork()调用实现多进程。
# 要实现跨平台的多进程，可以使用multiprocessing模块。
# 进程间通信是通过Queue、Pipes等实现的。