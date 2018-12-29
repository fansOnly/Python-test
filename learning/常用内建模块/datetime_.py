# !/usr/bin/env python3
# -*- coding: utf-8 -*-


# datetime
from datetime import datetime, timedelta, timezone

# 获取当前日期和时间
now = datetime.now()
print("获取当前日期和时间",now)
print(type(now))
print('*'*100)


# 获取指定日期和时间
dt = datetime(2018,12,14,10,48)
print("获取指定日期和时间",dt)
print('*'*100)


# datetime转换为timestamp
# 在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp。
# 注意Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。
dt2 = datetime(2018,12,14,10,48)
print("datetime转换为timestamp",dt2.timestamp())
print('*'*100)


# timestamp转换为datetime
t = 1429417200.0
dt3 = datetime.fromtimestamp(t)
dt4 = datetime.utcfromtimestamp(t)
print("北京时间", dt3)
print("UTC时间", dt4)
print('*'*100)


# str转换为datetime
# 注意转换后的datetime是没有时区信息的。
t2 = '2015-6-1 18:19:59'
dt4 = datetime.strptime(t2, '%Y-%m-%d %H:%M:%S')
print("str转换为datetime",dt4)
print('*'*100)


# datetime转换为str
now2 = datetime.now()
dt5 = datetime.strftime(now2, '%a, %b %d %H:%M')
print('datetime转换为str', dt5)
print('*'*100)


# datetime加减  - timedelta
now3 = datetime.now()
dt6 = now3 + timedelta(hours=10)
dt7 = now3 + timedelta(days=1)
dt8 = now3 + timedelta(days=1, hours=10)
print('当前时间', now3)
print('+10小时', dt6)
print('+1天', dt7)
print('+1天10小时', dt8)
print('*'*100)


# 本地时间转换为UTC时间
tz_utc_info = timezone(timedelta(hours=8))
now4 = datetime.now()
print('当前时间', now4)
now5 = now4.replace(tzinfo=tz_utc_info)
print('新的时区时间', now5)
print('*'*100)



# 时区转换
# 不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print('utc时间', utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('北京时间', bj_dt)
tokyo_dt = bj_dt.astimezone(timezone(timedelta(hours=9)))
print('基于北京时间计算的东京时间1', tokyo_dt)
tokyo_dt2 = utc_dt.astimezone(timezone(timedelta(hours=9)))
print('基于UTC时间计算的东京时间2', tokyo_dt2)
print('*'*100)



# 小结
# a/datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。
# b/如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。


# practice 1
# 假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp：

import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
    # pass
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    tz_infos = re.match(r'^UTC([\+\-])0?([\d]):00', tz_str)
    tz_info = int(tz_infos.group(1) + tz_infos.group(2))
    dtr = dt.replace(tzinfo=timezone(timedelta(hours=tz_info)))
    return dtr.timestamp()

# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')