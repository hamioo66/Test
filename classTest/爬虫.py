# -*- coding=UTF-8 -*-
"""
author:hamioo
date:2018/1/18
describle:爬取豆瓣小说
"""
from bs4 import BeautifulSoup
import urllib

helloword = '<p>hello world</p>'
soup_string = BeautifulSoup(helloword, "html.parser")
print
soup_string
# url = "http://www.qiushibaike.com/"
# page = urllib.urlopen(url)
# soup = BeautifulSoup(page,"html.parser")
# content = soup.find(attrs={"class": "content"})
# span = content.findAll(attrs={"tag": "span"})
# for s in span:
#     print s

res = urllib.urlopen("https://www.douban.com/tag/小说/?source=index")
soup = BeautifulSoup(res, "html.parser")
book_div = soup.find(attrs={"id": "book"})
book_a = book_div.findAll(attrs={"class": "title"})
describ = book_div.findAll(attrs={"class": "desc"})
dataset = []
for name, des in zip(book_a, describ):
    info = {
        "name": name.string,
        "des": des.string,
    }
    dataset.append(info)
for info in dataset:
    print
    info["name"] + info["des"]
