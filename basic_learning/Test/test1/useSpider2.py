#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re

#假设下面是一个源码，我想保存里面所有的链接
text = '<a href="www.baidu.com">....'
urls = re.findall('<a href=\"(.*?)\">',text,re.S)
print(urls)

#假设我需要爬取当前网页的头部
html = '''
<html>
<title>爬虫的基本知识</title>
<body>
……
</body>
</html>
'''
print(re.search('(<title>)(.*?)(</title>)',html,re.S).group(2))
#这里group(2)表示第二个括号的内容，如果正则里面有多个括号，这里可以通过group(i)返回第i个空格里的内容
#假设下面是一个贴吧的帖子地址，有很多页，每一页就是靠后面的pn=几来区分的，我们输出前10页的网址
Pages = 'http://tieba.baidu.com/p/4342201077?pn=1'
for i in range(10):
    print(re.sub('pn=\d','pn=%d'%i,Pages))


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
print(len(code2),'\n')
for item2 in code2:
    if len(item2) <=50:
        print(item2)

