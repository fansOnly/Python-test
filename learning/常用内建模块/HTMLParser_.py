# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# HTMLParser
# feed()方法可以多次调用，也就是不一定一次把整个HTML字符串都塞进去，可以一部分一部分塞进去。
# 特殊字符有两种，一种是英文表示的&nbsp;，一种是数字表示的&#1234;，这两种字符都可以通过Parser解析出来。

from html.parser import HTMLParser
from html.entities import name2codepoint

class HtmlParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)
    
    def handle_endtag(self, tag):
        print('</%s>' % tag)
    
    def handle_startendtag(self, tag, attrs):
        print('<%s />' % tag)
    
    def handle_data(self, data):
        print(data)
    
    def handle_comment(self, data):
        print('<!--',data,'-->')
    
    def handle_entityref(self, name):
        print('&%s:' % name)
    
    def handle_charref(self, name):
        print('#&%s:' % name)

htmltext = '''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>'''
parser = HtmlParser()
parser.feed(htmltext)
print('*'*100)


# practice 利用HTMLParser，可以把网页中的文本、图像等解析出来。
# https://www.python.org/events/python-events/
from urllib import request

class PythonOrgHtmlParser(HTMLParser):
    def __init__(self):
        super(PythonOrgHtmlParser, self).__init__()
        self.tag = ''
        self.prevtag = False
        self.events = list()
        self.event = dict()

    def handle_starttag(self, tag, attrs):
        # print('<%s>' % tag)
        if tag == 'h3' and ('class', 'event-title') in attrs:
            self.tag = 'title'
            self.prevtag = True
        elif tag == 'time':
            self.tag = 'time'
        elif tag == 'span' and ('class', 'event-location') in attrs:
            self.tag = 'location'
        else:
            self.tag = ''
    
    def handle_endtag(self, tag):
        # print('</%s>' % tag)
        pass
    
    def handle_startendtag(self, tag, attrs):
        # print('<%s />' % tag)
        pass
    
    def handle_data(self, data):
        # print(data)
        if self.tag == 'title':
            self.tag == ''
        elif self.prevtag and self.tag == '':
            self.event['title'] = data
            self.prevtag = False
        elif self.tag == 'time':
            self.event['time'] = data
        elif self.tag == 'location':
            self.event['location'] = data
            self.events.append(self.event)
            self.tag = ''
            self.event = dict()
        else:
            self.tag = ''
    
    def handle_comment(self, data):
        # print('<!--',data,'-->')
        pass
    
    def handle_entityref(self, name):
        # print('&%s:' % name)
        pass
    
    def handle_charref(self, name):
        # print('#&%s:' % name)
        pass

with request.urlopen('https://www.python.org/events/python-events/', timeout=4) as f:
    data = f.read()

parser = PythonOrgHtmlParser()
parser.feed(data.decode('utf-8'))
print('-'*100)
print(parser.events)
print('-'*100)