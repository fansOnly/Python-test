# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 分布式进程
import random, time, queue
from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = queue.Queue()
# 获取任务的队列
result_queue = queue.Queue()
# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# 绑定端口5000, 设置验证码'abc':
manager = QueueManager(address=('', 5000), authkey=b'abc')
# 启动Queue
manager.start()
# 获得通过网络访问的Queue对象:
task = manager.get_task_queue()
result = manager.get_result_queue()
# 放几个任务进去:
for i in range(10):
    print('put task %s' % i)
    task.put(i)
# 获取任务
for i in range(10):
    r = result.get(timeout = 10)
    print('get result %s' % r)
# 关闭:
manager.shutdown()
print('manager exit...')