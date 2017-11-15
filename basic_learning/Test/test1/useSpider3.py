#/usr/bin/env python3
# coding: utf-8 -*-
import re
import requests


# 1. 用findall查找所有
# url = "http://www.jianshu.com/p/74b94eadae15"
# result = requests.get(url).text
# code = re.findall('<code.*?>(.*?)</code>',result,re.S)
# for item in code:
#     print(item,'\n')
# print(111111111111111111111111111)


url2 = "http://www.imooc.com/"
result2 = requests.get(url2).text
code2 = re.findall('<h3.*?>(.*?)</h3>',result2,re.S)
for item2 in code2:
    if len(item2) <=50:
        print(item2)
print(len(code2))

