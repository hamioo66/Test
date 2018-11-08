# -*- coding=UTF-8 -*-
"""
author:hamioo
date:2018/11/8
describle:
"""
from urllib import request, parse
import requests
# 例一
response = request.urlopen('https://www.python.org')
print(response.read().decode('utf-8'))
print(type(response))
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))

# 例二
url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible;MSIE;Windows NT)',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'hamioo'
}
data = bytes(parse.urlencode(dict), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))

# 例三
data= {
    'name':'germey',
    'age':'22'
}
r = requests.get('http://httpbin.org/get',params=data)
print(r.text)
print(r.json())
print(type(r.json()))


# 例三
r1 = requests.get('https://github.com/favicon.ico')
with open('favicon.ico','wb') as f:
    f.write(r.content)

