# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# XML

# DOM vs SAX
# 操作XML有两种方法：DOM和SAX。DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。

# 在Python中使用SAX解析XML非常简洁，通常我们关心的事件是start_element，end_element和char_data，准备好这3个函数，然后就可以解析xml了。
# 需要注意的是读取一大段字符串时，CharacterDataHandler可能被多次调用，所以需要自己保存起来，在EndElementHandler里面再合并。

from xml.parsers.expat import ParserCreate

class DefaultSaxHandle(object):
    def start_element(self, name, attrs):
        print('sax: start_element %s, attrs: %s' % (name, str(attrs)))
    
    def end_element(self, name):
        print('sax: end %s' % name)
    
    def char_data(self, text):
        print('sax: char_data %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandle()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)
print('*'*100)


########################################################################################################
# 生成XML - 拼接字符串
# L = []
# L.append(r'<?xml version="1.0"?>')
# L.append(r'<root>')
# L.append(r'some & data'.encode('utf-8'))
# L.append(r'</root>')
# return ''.join(L)


# practice - 请利用SAX编写程序解析Yahoo的XML格式的天气预报，获取天气预报：
from xml.parsers.expat import ParserCreate
from urllib import request

class WeatherSaxHandle(object):
    def __init__(self):
        self.forecast = list()
        self.city = ''

    def start_element(self, name, attrs):
        print('sax: start_element %s, attrs: %s' % (name, str(attrs)))
        if name == 'yweather:location':
            self.city = attrs['city']
            # print('城市名称: %s' % attrs['city'])
        if name == 'yweather:forecast':
            # print('获取天气列表', attrs)
            self.forecast.append({'date': attrs['date'], 'high': attrs['high'], 'low': attrs['low']})
    
    def end_element(self, name):
        pass
        # print('sax: end %s' % name)
    
    def char_data(self, text):
        pass
        # print('sax: char_data %s' % text)

def parseXml(xml_str):
    # print(xml_str)
    handler = WeatherSaxHandle()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml_str)
    print('-'*100)
    print(handler.city, handler.forecast)
    print('-'*100)
    return {
        'city': handler.city,
        'forecast': handler.forecast
    }

# 测试:
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))
assert result['city'] == 'Beijing'