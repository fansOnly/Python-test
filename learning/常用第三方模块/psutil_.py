# !/usr/bin/env python3
# -*- coding: utf-8 -*-


# psutil
# 它不仅可以通过一两行代码实现系统监控，还可以跨平台使用，支持Linux／UNIX／OSX／Windows等，是系统管理员和运维小伙伴不可或缺的必备模块。

import psutil

print('-'*100)
print('cpu数量', psutil.cpu_count())
print('-'*100)
print('cpu物理核心', psutil.cpu_count(logical=False))
print('-'*100)
print('统计CPU的用户／系统／空闲时间：', psutil.cpu_times())
print('-'*100)

# CPU使用率，每秒刷新一次，累计10次：
# print('CPU使用率')
# for i in range(10):
#     print(psutil.cpu_percent(interval=1, percpu=True))
# print('-'*100)


# 获取内存信息
print('物理内存')
print(psutil.virtual_memory())
print('-'*100)
print('交换内存')
print(psutil.swap_memory())
print('-'*100)


# 获取磁盘信息
print('磁盘分区信息')
print(psutil.disk_partitions())
print('-'*100)
print('磁盘使用情况')
print(psutil.disk_usage('/'))
print('-'*100)
print('磁盘IO')
print(psutil.disk_io_counters())
print('-'*100)


# 获取网络信息
print('获取网络读写字节／包的个数')
print(psutil.net_io_counters())
print('-'*100)
print('# 获取网络接口信息')
print(psutil.net_if_addrs())
print('-'*100)
print('# 获取网络接口状态')
print(psutil.net_if_stats())
print('-'*100)
print('获取当前网络连接信息')
print(psutil.net_connections())
print('-'*100)



# 获取进程信息
print('# 所有进程ID')
print(psutil.pids())
print('-'*100)
print('# 获取指定进程ID')
p = psutil.Process(8840)
print('进程名称', p.name())
print('# 进程exe路径', p.exe())
print('# 进程工作目录', p.cwd())
print('# 进程启动的命令行', p.cmdline())
print('# 父进程ID', p.ppid())
print('# 子进程列表', p.children())
print('# 进程状态', p.status())
print('# 进程用户名', p.username())
print('# 进程创建时间', p.create_time())
# print('# 进程终端', p.terminal())
print('# 进程使用的CPU时间', p.cpu_times())
print('# 进程使用的内存', p.memory_info())
print('# 进程打开的文件', p.open_files())
print('# 进程相关网络连接', p.connections())
print('# 进程的线程数量', p.num_threads())
print('# 所有线程信息', p.threads())
print('# 进程环境变量', p.envirson())
print('# 结束进程', p.terminate())