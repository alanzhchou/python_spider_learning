#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from bs4 import BeautifulSoup
import requests

def tryJson(response):
    try:
        result = response.json()
        return result
    except Exception as e:
        print("exe json() error")

class Info(object):
    def __init__(self):
        self.urls = []
        self.datas = []
        self.jsons = {}
        self.files = {}
        self.cookies = {}
        self.setAsExample()

    def setAsExample(self):
        self.urls.append("http://httpbin.org")
        self.urls.append("http://httpbin.org/cookies")
        self.urls.append("http://httpbin.org/get")
        self.urls.append("http://httpbin.org/post")
        self.urls.append("http://www.baidu.com")
        self.datas.append({'key1': 'value1', 'key2': 'value2'})
        self.jsons["first_name"] = "chou"
        self.jsons["last_name"] = "alan"
        self.files["test.txt"] = open('test.txt', 'rb')
        self.cookies["cookie1"] = "aaaaaaaaaaaaaaaaaaaaaaaaaaa"
        self.cookies["cookie2"] = "bbbbbbbbbbbbbbbbbbbbbbbbbbb"

info = Info()

# 文件以post上传
# response = requests.post(info.urls[3],files=info.files)
# print(response.text)

#获取目标网站的cookie
# response = requests.get(info.urls[1],cookies=info.cookies)
# print(response.text)


#建立session保持长久会话
# session = requests.session()
# session.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
# session.headers.update({'Chinese_name':'zhouheng'})
# response = session.get('http://httpbin.org/headers',
#                        headers={'Chinese_name':None})
# print(response.text)

#https的SSl验证
#requests请求https时，默认请求网站的证书，若证书失效，则无法请求（报错）
#可通过verify来取消SSL证书验证，正常返回可以https网页内容
# try:
#     r1 = requests.get('https://kyfw.12306.cn/otn/', verify=False)
#     print(r1.text)
# except Exception as e:
#     print(e.args)
#
# r2 = requests.get('https://github.com', verify=True)
# print(r2.text)

html ='''
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Hello,world!</title>
	<link rel="shortcut icon" href="http://seeu.studio/favicon.ico" type="image/x-icon"/>
</head>
<style>
	body{background:#FFF url
("http://seeu.studio/seeu/images/frontend/mockup1.png") no-repeat left 0}
	div{height: 40px; width: 508px; border: 5px groove #B8E986; position: 
absolute; top: 35%; left: 50%}
	img{height: 40px; width: 40px}
	input {line-height: 32px; width: 400px;	size="30"}
	button{line-height: 32px}
</style>
<body>
<div>
	<img src="http://seeu.studio/seeu/images/seeu/product/gpa_sys.png" 
alt="search" style="float: left;"/>
	<form action="http://www.baidu.com/baidu" target=""> 
	    <a href="">aaa<!--this is a comment--></a>
		<input type=text name=word><button>search</button>
	</form>
</div>
<div>
	<img src="http://seeu.studio/seeu/images/seeu/product/gpa_sys.png" 
alt="search" style="float: left;"/>
	<form action="http://www.baidu.com/baidu" target=""> 
		<input type=text name=word><button>search</button>
	</form>
</div>
</body>
</html>'''

#BeautifulSoup中共四个类型：Tag（标签整体），NavigableString（标签内内容）
#BeautifulSoup(相当于html的document)，comment（注释内容）

#直接解析字符串或者打开文件生成节点对象
soup = BeautifulSoup(html,"lxml")

#直接指定指定的DOM节点，可获取第一个满足条件的节点信息
title = soup.title
head = soup.head
div = soup.div
a = soup.a
img = soup.img

# print(title)
# print(head)
# print(div)
# print(img)

#type也可验证节点的类型，都是tag，都有两个重要的属性，是 name 和 attrs
# lib = [soup,title,head,div,img]
# for ele in lib:
#     print(type(ele),ele.name,ele.attrs)

#可单独用字典形式或get方法直接浏览属性
# print(img["src"])
# # print(img.get("src"))

#可以直接对节点的属性和内容修改
# img["class"] = "newClass"
# print(img)
# #删除属性
# del img["class"]
# print(img)

#####################################################################
#2.NavigableString类型，用string调用
# print(type(title.string),title.string)

####################################################################
#3.BeautifulSoup对象相当于document
# print(soup.name)

#####################################################################
#4.comment（注释内容，不包括注释符号）特殊类型的NavigableString
# print(type(a.string),a.string)



#######################################################
#更多高级和批量操作

#遍历文档树
#列表输出-contents
# print(type(a.contents),a.contents)

#children它返回的不是一个 list，而是list生成器，可以通过它遍历获取所有子节点。
# print(soup.children)
# for child in div.children:
#     print(child)

#.contents 和 .children 属性仅包含tag的直接子节点
#.descendants 属性可以对所有tag的子孙节点进行递归循环，
# 和 children类似，我们也需要遍历获取其中的内容。
# for toChild in div.descendants:
#     print(toChild)

#.string返回可能的唯一节点内容，如果含多个节点或同时存在内容和注释则无法返回，返回为none
# print(soup.button.string)
# print(a.string)

#多个内容用strings,stripped_strings(可去除空白，即空格或空行)
# for arg in soup.form.strings:
#     print(arg)

for arg in soup.form.stripped_strings:
    print(arg)