#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#python面向对象

#1.最重要的概念就是类，
#python中通过关键字class定义类，
#类名开头通常大写，之后的()内代表继承的类，若没有的话默认从object类中继承
class Student(object):
    #构造方法
    def __init__(self,Id,Name):#直接定义类属性
        self.__studentID = Id
        self.__studnetName = Name

    def out(self):
        print(self.__studentID,end='\t')
        print(self.__studnetName)
x = Student(11510629,"AlanChou")
x.out()
print()

#python中的类在被继承时其private的属性虽然也被继承，但在子类中却无法正确调用
#所以在继承含私有属性的类的时候，记得在父类的代码中加入操作或返回私有属性的方法

#2.方法：又称函数，python中用def xxx（xxx）：声明
#这里只说下特别的传参的顺序在python中显得不是很重要，只要标定形式参数赋值即可
def printinfo(name,age):
    #打印传入的姓名和年龄
    print('Name: ',name,end='\t')
    print('age: ',age)

printinfo(age=20,name='Alan Chou')
#同时在定义函数体时可指定默认的参数值：
#在调用时缺省没传入该参数，则函数运行时按默认的参数值运行
def printinfo1(name,age=35):
    print('Name: ', name, end='\t')
    print('age: ', age)

printinfo1(name='Alan Chou')
print()
#函数的不定长参数,加
def manyNumbers(args, *var_args_tuple):
    #打印任何传入的参数
    print('输出：')
    print(args,'\t接下来是变长的参数：')
    for i in var_args_tuple:
        print(i,end='\t')
    print()

manyNumbers('here is the first element',10,20,30,40)
print()

#3.匿名函数lambda
#声明形式为  lambda arg1,arg2...:function
#匿名函数也可以设定默认值
sum1 = lambda a1,a2=100: a1+a2
print('测试匿名函数：',sum1(10,20))
print('测试匿名函数(带默认参数)：',sum1(10))
print()

#PS,大多数脚本语言的通性，最小的作用域为函数的作用域，所以以下的for，while
#等不会新增变量的作用域，在外部依旧可以调用（遍历字典，默认遍历的为keys）
testArea = {11510629:'Alan',11510630:'Jack',11510631:'Dean'}
for i in testArea:
    pass
print(i)
print()
#在进行函数嵌套时，使得外部作用域可以调用内部的变量，则要在内部声明时使用nolocal
def outer():
    outer_number = 10
    def inner():
        nonlocal outer_number
        outer_number = 20
        print(outer_number)
    inner()
    print(outer_number)
outer()
print()

#4.转化字典
#一种特殊的函数参数传入的声明，可以把多个关键字转化为字典，
#包括字典的变量名，key和value
#声明为def xxx(xxx,xxx,**kwargs):#xxx,xxx表示变量名，**kwargs生成字典
def toDitctionary(university,**kwargs):
    print(university,kwargs)
toDitctionary('NKD',grade = '15',ban = '21')
print()



