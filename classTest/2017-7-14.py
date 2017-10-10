# -*- coding:UTF-8 -*-
import json
data=[{'a':1,'b':2,'c':3}]
json=json.dumps(data)
print json

import urllib
import urllib2
postdata=urllib.urlencode({'username':'XXXXX','password':'XXXXX','continueURI':'http://www.verycd.com','login_submit':'登录'})
headers={'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
req=urllib2.Request(url='http://secure.verycd.com/signin/*/http://www.verycd.com/', data = postdata, headers = headers)
