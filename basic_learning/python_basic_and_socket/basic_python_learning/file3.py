#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#python内置默认为unicode编码，所以用汉字做变量名是合法的，如下：
中国 = "China"
print(中国)
print()

#python3.X，新增的bytes类型，对应八位串, 声明用b''声明
a = 'China'
b = b'China'
print(type(a))
print(type(b))
#str和bytes对象可以用.encode()和.decode()相互转换
s1 = a.encode()
s2 = b.decode()
print(type(s1))#a-->str, s1-->bytes
print(type(s2))#b-->bytes, s2-->str
print()

#1.python的运算符：
#常见的 + - * / % **(幂，次方) //(取整除，返回商的整数部分)
c = 5
d = 3
print(c+d)#8
print(c-d)#2
print(c*d)#15
print(c/d)#1.66666...
print(c%d)#2
print(c**d)#125
print(c//d)#1
print()

#2.python的比较运算符，赋值运算符，按位运算符
#比较运算符，都是常规的==     !=      >       <       >=      <=
#赋值运算符，=     +=      -=      /=      %=      **=        //=
#按位运算符，0b表示二进制，0o表示8进制，0x表示十六进制
#与：&，或|，异或^，取反~，左移<<，右移>>
e = 0b10111#1*16+1*4+1 = 21
f = 0b11101#1*16+1*8+1*4+1*2+1 = 31
print(bin(e))
print(bin(f))
print(bin(e&f))#10101
print(bin(e|f))#11111
print(bin(e^f))#1010
print(bin(~e))#???默认将最高位看做符号位？
print(bin(e>>2))#101
print(bin(e<<2))#1011100
print()

#3.逻辑运算符
#and，or，not
#x and y
#布尔"与"-如果x为False，x and y返回 False，否则它返回y的计算值。
#x or y
#布尔"或"-如果x为非0，x or y返回x的值，否则它返回y的计算值。
#not x
#布尔"非"-如果x为True，not x返回 False，即返回反x。
g = 10
h = 20
print(g and h)#20
print(g or h)#10
print(not g)#False
print()

#4.成员运算符
#in,在指定的序列中查找是否存在对应值
#not in 在指定的序列判断是否不存在对应值
i = 3
tuple1 = (2,3,3.1415,'2')
print(i in tuple1)
print(i not in tuple1)
print()

#5. 身份运算符
#用来比较两个对象的存储单元
#is：判断是否引用来自同一个对象
#is not：判断是否引用来自不同对象
#is与==的区别:
#同java中类似，==用来进行值比较，如下的2==2.0返回为true，
# 而is相当于js中的 === ？既要值相等也要类型相等
'''
Python中的对象包含三要素：id、type、value
其中id用来唯一标识一个对象，type标识对象的类型，value是对象的值
is判断的是a对象是否就是b对象，是通过id来判断的-结合type和value
==判断的是a对象的值是否和b对象的值相等，是通过value来判断的
'''
j = 2
k = 2
L = 2.0
print(j is k)#true
print(j is L)#flase
print(j == L)#true
print()

#6.条件语句
#if():      else:       不同的是elseif被替代为elif
#在python中没有switch语句
M = 20
while(M != 0):
    if(M%3 == 1):
        print("1\t",end='')
    elif(M%3 == 2):
        print("2\t",end='')
    else:print("0\t",end='')
    M-=1
print()
#猜数字小游戏：
# print("猜数字游戏：")
# N = 7
# guess = -1
# while guess != N:
#     guess = int(input("输入猜的数字："))
#
#     if guess == N:
#         print("恭喜！你猜对了")
#     elif guess < N:
#         print("猜的数字小了。。。")
#     elif guess > N:
#         print("猜的数字大了。。。")
# print()

#7.循环语句
#python里提供了，for和while的循环（没有do...while的循环）
#循环内支持break，continue操作
#特殊的循环或者说是暂时性的填补的空语句
#
#特殊的python里的循环提供了else语句块，
#while...else在循环条件为false时执行，即循环非break的正常退出后执行else语句
N = 20
while N>6:
    print(N,end='\t')
    N-=1
else:print("N = " + str(N))
print()

O = 20
while O>6:
    print(O,end='\t')
    O-=1
    if O==6:
        break
else:print("N = " + str(N))#这里不会打印N = 6
print()

#for循环也有else，也是在正常判断而非break的退出后执行
#for的遍历
#1. 用in
languages = ["C", "C++", "Python", "Perl", "Java"]
for a in languages:
    print(a,end='\t')
print()

#2.range()函数
#用来遍历数字序列
for i in range(5):
    print(i,end='\t')
print()
#指定range范围
for i in range(5,9):#同列表中取值类似，都是左闭右开
    print(i,end='\t')
print()
#同时指定步长
for i in range(0,10,2):#依次为起点，终点，步长
    print(i,end='\t')
print()
#结合range()和len()遍历一个序列，
#languages = ["C", "C++", "Python", "Perl", "Java"]
for i in range(len(languages)-2):
    print(i,languages[i])
#用range来创建列表:
P = list(range(0,100,10))
for pi in P:
    print(pi,end='\t')
print(),print()
#用enumerate（枚举）
tuple12 = ('A','B','C','D','E','F')
for i,j in enumerate(tuple12):
    print(i,end=' '),print(":",end=' '),print(j)



