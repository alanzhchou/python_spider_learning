#!/usr/bin/env python3
# coding: utf-8 -*-
import re
import requests

url = 'https://github.com/timeline.json'
response1 = requests.get(url)
header = response1.headers

info = []
for headerItem in header:
    temp = []
    temp.append(headerItem)
    if len(header.get(headerItem)) < 40:
        temp.append(header.get(headerItem))
    else:
        temp.append('too long')
    info.append(tuple(temp))

info = tuple(info)

# print(response1.status_code)
# json = response1.json()
# for jsonItem in json:
#     print(jsonItem,":",json.get(jsonItem))


####################################
# post请求
# payload = {'key1':'value1','key2':'value2'}
# response2 = requests.post("http://httpbin.org/post",data=payload)
# print(response2.content.decode())






