# -*- coding=UTF-8 -*-
"""
author:hamioo
date:2018/1/22
describle:
"""
import urllib
import urllib2
values = {}
values['username'] = "986263137"
values['password'] = "moran@@**811426"
# user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
# headers = {'User-Agent':user_agent}
data = urllib.urlencode(values)
url = "http://passport.csdn.net/account/login"
geturl = url + "?" + data
print geturl
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()