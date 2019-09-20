#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#python中的异常处理及文件I/O流

#1.异常
'''
用try：
except xxx：
来捕获异常
'''
#捕获用户不正常输入而退出的异常
'''
while True:
    try:
        x = int(input('enter a number'))
        break
    except ValueError:
        print('No valid number. Try again')
print()
'''

#2.判断异常发生及其执行
#先执行try，没有异常的话跳过except
#try语句中发生异常的话，余下未执行的部分会被忽略
#！！！只有当异常类型和except抛出的异常类型相同时，执行except中的语句
#会被继续执行，执行完毕后不再回到try语句，而是执行之后的代码
'''
while True:
    try:
        x = int(input('enter a number'))
        break
    except ValueError:
        print('No valid number. Try again')
print('继续执行剩下的语句')
print()
'''
#一个try语句可以匹配多个异常，而最多只会进入其中一个
#！！而一个except可以包含多个异常类型，需将多个包在括号里形成元祖（tuple）
'''
except (RuntimeError, TypeError, NameError):
    pass
'''
#在except之后可以接一个finally语句，接在except后执行

#3.python的输入输出
#（1.print
#（2.文件对象的write()方法-sys.stdout
#用str.format来格式化输出
#转成字符串str()和repr()两个函数

#str.format()的使用
#{}及其中的字符会被format()中的参数替代
#有时候{}中会存在数字，用来标定传入的对象在format中传入的位置
print('{}网址:"{}!"'.format('南方科技大学','www.sustc.edu.cn'))
print('谷歌的网址：{1}，百度的网址：{0}'.format('www.baidu.com','www.google.com'))
#有时候在{}中有关键字声明了相关变量，则在format传入是需要对应赋值
print('{name}的网址：{site}'.format(site='www.alanchou.space',name='Alan'))

#str.format的基本使用：
#'!a','!s','!r'分别表示使用ascii(),使用str()，使用repr()(用在{}中)
print('{}的网址：{!r}'.format('github','www.github.com'))
#注意输出的网址是带引号的

#str.foramt()还可以指定输出字符的长度，如保留三位有效数字等
import math
print('PI的值保留三位小数是：{0:0.3f}'.format(math.pi))
print()
#4.读取键盘输入input
# str = input('输入字符可立即打印：')
# print('刚才输入的是',str)

#进行特定运算，如进行数学运算等就要对输入做个类型转换
'''
while True:
    try:
        x = int(input('enter a number'))
        break
    except ValueError:
        print('No valid number. Try again')
print(x**2)
'''

#5.open()进行读写文件
#open(filename,mode)将返回一个读取的file对象
#这里的mode表示打开文件的方式，包括只读，写入，追加等
#只读：(如果文件不存在则抛出IOError的异常)
f = open('test.txt','r')
#ps:读取视频，图片等二进制编码的文件用'rb'读取

#打开成功后可以用read()来读取内容了,read()读取为内存中的一个对象，
#当文件过于庞大，在内存中不宜直接读取的话，可以用readline(s)分行读取
#还可以用read(size)按size个字节的速度反复读取
print(f.read())
# print(f.readline())
# lines = f.readlines()#readlines,分行读取为一个可操作的序列
# for line in lines:
#     print(line)

#6.操作完后用close()关闭文件，避免占用资源
f.close()
print()

#7.python对文件IO的异常处理
#为了保证是否正常读取写入文件都能在读完后正确关闭，要用finally来执行：
try:
    f = open('test.txt','r')
    print(f.read())
finally:
    if f:
        f.close()
print()
#为了避免每次写得这么繁琐，python引入with来自动调用close
with open('test.txt','r') as f:
    print(f.readline())
print()

#open读取的编码问题，open默认读取自身的utf-8编码的数据，要指定编码方式
#可以用encoding参数，在读取中可能会混入一些非法编码的字符，可用errors参数
#表示遇到编码错误后的处理,比如直接忽略
#如：
#f = open('C:\\Users\LENOVO\Desktop\\test.txt','r',encoding='gbk',errors='ignore')


#8.写文件，与读文件类似
#open调用时传入写入的标识符w或者wb等
#用于系统是先将数据写入内存，在关闭前的空闲时间写入，只有close
#时才会保证调用写入文件
#用with来保证写入
'''
with open('test.txt','w') as f:
    f.write('Hello,world')
'''