# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# urllib
from urllib import request


#################################################################################################
# Get
# urllib的request模块可以非常方便地抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应：
with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    # print('Data: ', data.decode('utf-8'))
    with open('F:\python\Python-test\learning\常用内建模块\files\liao.html', 'w') as w:
        w.write(data.decode('utf-8'))
print('*'*100)


# 使用Request对象，通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器
req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    data = f.read()
    print('Status: ', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    # print('Data: ', data.decode('utf-8'))
    with open('F:\python\Python-test\learning\常用内建模块\files\douban.html', 'w') as w:
        w.write(data.decode('utf-8'))
print('*'*100)



#################################################################################################
# Post
# 如果要以POST发送一个请求，只需要把参数data以bytes形式传入。
from urllib import request, parse

print('login in weino...')
# username = input('请输入账号:')
# password = input('请输入密码：')
login_data = parse.urlencode([
    # ('username', username),
    # ('password', password),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])
req = request.Request('https://passport.weibo.cn/sso/logi')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data = login_data.encode('utf-8')) as f:
    print('Status: ', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    # print('Data: ', f.read().decode('utf-8', 'ignore'))
    with open('F:\python\Python-test\learning\常用内建模块\files\weibo.html','w') as w:
        w.write(f.read().decode('gbk', 'ignore'))
print('*'*100)



# Handler
# 如果还需要更复杂的控制，比如通过一个Proxy去访问网站，我们需要利用ProxyHandler来处理
# proxy_handler = request.ProxyHandler({'http': 'http://www.example.com:3128/'})
# proxy_auth_handler = request.ProxyBasicAuthHandler()
# proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
# opener = request.build_opener(proxy_handler, proxy_auth_handler)
# with opener.open('http://www.example.com/login.html') as f:
#     pass
# print('*'*100)



# practice 利用urllib读取JSON，然后将JSON解析为Python对象：
import json
def fetch_data(url):
    with request.urlopen(url) as f:
        data = f.read()
    return json.loads(data.decode('utf-8'))

# 测试
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
data = fetch_data(URL)
print(data)
assert data['query']['results']['channel']['location']['city'] == 'Beijing'
print('ok')