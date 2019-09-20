#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#1. python可以用\来使得一行较长的语句分行编写
total = 100+\
        200+\
        300
print(total)
print()


#2.语句中有类似代码块声明时不用、分行
total2 = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday']
print(total2)
print()


# 3.python中可以用单双三引号来表示字符串，但开始和结尾必须相同
word = 'word'
sentence = "这是一个句子。 "
paragraph = """这是一个段落。包含了多个语句：
    1.语句一：
    2.语句二：
    3.语句三：
    """
print(word + "\n" + sentence+"\n" + paragraph)
print()

#4.python中单行注释为#
'''
多行注释可用三个单引号或者三个双引号
多行注释可用三个单引号或者三个双引号
多行注释可用三个单引号或者三个双引号
'''
"""
多行注释可用三个单引号或者三个双引号
多行注释可用三个单引号或者三个双引号
多行注释可用三个单引号或者三个双引号
"""

#5.input接受用户输入数据
#input("\n\nPress the enter key to exit.")

#6.多个缩进相同的行构成代码组
#像if，while，for，def这种条件或者复合语句，结尾加：冒号表示接下来的动作
judge = True
if(judge):
    print(judge)
    judge = False

a = 1
sum = 0
while(a<51):
    sum+=a
    print(a,end='')
    print("\t",end='')
    if(a%10 == 0):
        print()
    a+=1
print()


def printSum(sum):
    print('25 * 51 = ',sum)
printSum(sum)
print()

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
print()


#7.截取范围,python中的下标也是从0开始[start：end]，的截取方式，默认为左闭右开，即截取end-start个字符，从start开始
s = "IlovePython"
print(s[1:5])
