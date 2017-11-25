#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re

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
	    <a href="1111">aaa<!--this is a comment--></a>
	    <a href="2222">bbbb<!--this is another comment--></a>
		<input type=text name=word><button>search</button>
	</form>
</div>
</body>
</html>'''

#直接解析字符串或者打开文件生成节点对象
soup = BeautifulSoup(html,"lxml")

#直接指定指定的DOM节点，可获取第一个满足条件的节点信息
title = soup.title
head = soup.head
div = soup.div
a = soup.a
button = soup.button
img = soup.img

#遍历节点
#************************************************************

#1.父节点-.parent,不只可针对节点，
# 也可针对节点内的内容取父节点,内容的父节点即为包括该内容的直接节点
# print(button.parent,'\n',button.string.parent)

#2.递归获取全部父节点-.parents
# for parent in button.string.parents:
#     print(parent.name)

########################################################
#1. 浏览兄弟节点
#用.next_sibling,  .previous_siblong
#属性通常是字符串或空白，因为空白或者换行也可以被视作一个节点，
# 所以得到的结果可能是空白或者换行,这里跳过了一个空白
# print(a.next_sibling.next_sibling)

#next_siblings,   .previous_siblings获取全部兄弟节点的迭代器
# for ele in a.next_siblings:
#     print(ele)

############################################################
#2.获取前后节点，#以全体为跨度，(使用时也要跳过空格等)
#.next_element,previous_element
# print(head.next_element.next_element)

#获取前后所有节点的迭代器，包括了空格等
#.next_elements,previous_elements.
# for ele in a.next_elements:
#     print(repr(ele))

#***************************************************************
#2.搜索文档树

########################################################3333
##1.find_all( name , attrs , recursive , text , **kwargs )
# print(div.find_all("a"))

##传入列表则会返回各元素匹配的节点
# print(div.find_all(["a","input"]))

##传入Ture，则返回所有tag，（即存在的），但不会返回字符串等
# for ele in div.find_all("form")[0].find_all(True):
#     print(ele)

#还可以将筛选的方法当做参数输入
#def has_class_but_no_id(tag):
#    return tag.has_attr('class') and not tag.has_attr('id')
#soup.find_all(has_class_but_no_id)

#############################################################
#2.关键字搜索：keyword,可以同时指定多个
# print(soup.find_all(alt="search"))
# print(soup.find_all(alt="search",style="float: left;"))
#####---tips,由于class是python关键字，作为属性传入时，写作：class_
#即加一个下划线

#############################################################
#3. text参数，返回值为所有的节点中的字符串内容经过过滤的结果,
#接受参数可为字符串，正则列表和True
# print(soup.find_all(text="aaa"))
# print(soup.find_all(text=["aaa","bbbb"]))
# print(soup.find_all(text=re.compile("a.*")))

##############################################################
#4.limit参数指定返回的数量
# print(soup.find_all("a",limit=1))
# print(soup.find_all("a",limit=2))

##############################################################
#5.recursive参数，指定是否递归查找，因为默认递归，
# 要搜索直接节点，设置为False
# print(soup.find_all("a"))
# print(soup.find_all("a",recursive=False))


#*************************************************************
#find方法，find( name , attrs , recursive , text , **kwargs )
#返回满足条件的第一个元素,除此与find_all基本相同
# print(a.find_next_sibling("a"))
# print(a.findParent())



#***************************************************************
#3.重要**********************************css选择器查找
# print(soup.select("a"))
# print(soup.select_one("a"))

###########
#通过子标签查找：head > meta,注意中间必须要有空格
print(soup.select("head > meta"))
#通过tag+属性查找
print(soup.select("a[href='2222']"))







