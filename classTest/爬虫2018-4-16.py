# -*- coding=UTF-8 -*-
"""
author:hamioo
date:2018/1/2
describle:BeautifulSoup 模块解析HTML
"""
import requests,bs4   # 导入BeautifulSoup
res = requests.get('http://baidu.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)
type(noStarchSoup)
