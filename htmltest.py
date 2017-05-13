# -*- coding: utf-8 -*-
from urllib.request import urlopen
from urllib import request
from bs4 import BeautifulSoup as bs
import re
import urllib
import os
# 创建文件夹,从网站下载图片
cur_dir = 'D:'
folder_name = 'image'
if os.path.isdir(cur_dir):
    os.mkdir(os.path.join(cur_dir, folder_name))


req = urlopen("http://www.nsre.cc/?qqdrsign=01400").read()
def show(reqItem,n):
    soup = bs(reqItem, "html.parser")
    listImgs = soup.find_all("img")
    for img in listImgs:
        # if re.search("\.(jpg)$",img["data-echo"]):
        imgUrl = "http://www.nsre.cc/" + img["data-echo"]
        #匹配字符串
        if imgUrl.startswith("http://www.nsre.cc/data") and imgUrl.endswith(".jpg"):
            print(imgUrl)
            #urllib.request.urlretrieve(imgUrl, "F:/image/%d.jpg" % j)
            urllib.request.urlretrieve(imgUrl, "D:/image/%d.jpg" % n)
            n += 1
    return n
# 使用BeautifulSoup解析,参数2解析器
soupAll = bs(req, "html.parser")
listAs = soupAll.find_all("a")
n=0
for a in listAs:
    aUrl = a["href"]
    if aUrl.startswith("http://www.nsre.cc/thread-"):
        print(aUrl)
        reqItem = urlopen(aUrl).read()
        n=show(reqItem,n)
        n+=1
