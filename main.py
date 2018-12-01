#!/usr/bin/python
# -*- coding: UTF-8 -*-
# main.py

"Test file."
__author__ = "Jing Mike"

import math
import time
import calendar
import os
from datetime import datetime
import mypackage.mytool
import os
import requests
from lxml import html

headers = {
'Host': 'www.163.com',
'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
'Connection': 'keep-alive',
'Pragma': 'no-cache',
'Cache-Control': 'no-cache',
'Upgrade-Insecure-Requests': '1',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) '
'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
}

def crawl(url: object) -> object:
    resp = requests.get(url, headers=headers)
    page = resp.content
    root = html.fromstring(page)
    image_urls = root.xpath('//img[@data-original]/@data-original')
    for image_url in image_urls:
        print(image_url)

def myfun():
    mypackage.mytool.mytoolfun()
    datetime.now()


if __name__ == "__main__":
    crawl('https://www.163.com/')
