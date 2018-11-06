# -*- coding=UTF-8 -*-
"""
author:hamioo
date:2018/10/11
describle:接口自动化  requests库
"""


# import requests
# import urllib
# r = requests.get('https://api.github.com/user')
# print(r.status_code)
# print(r.text)

import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context()
response = urllib.request.urlopen('https://www.python.org')
print(response.read().decode('utf-8'))
print(type(response))
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))