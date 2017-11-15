#/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import re

'''
熟悉python正则表达式
'''

# 1. match/group查找匹配情况，可根据分组来返回不同的匹配结果，默认flags在首位开始匹配
# group()即为group(0)，用span()处理match的返回对象则可返回match的开始和结尾的index
agrs = 'abcABC'
print(re.match('([a-zA]*)',agrs,flags=0).group())

# 分组match
line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) (.*)', line, re.M|re.I)
if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")
# groups()则返回全部匹配时各组匹配的元组
print(matchObj.groups(),'\n')


# 2.findall将所有已匹配的字符串以元组形式返回
threeLine = '''
aaa
123
asd465
'''
result1 = re.findall('([0-9]{3}?)',threeLine,re.S)
print(result1)

# 3.search扫描整个字符串并返回第一个匹配成功的
result2 = re.search('([0-9]{3}?)',threeLine,re.S)
print(result2.group())

# 4.sub用来替换
result3 = re.sub('([0-9]{3}?)','~',threeLine,re.S)
print(result3)