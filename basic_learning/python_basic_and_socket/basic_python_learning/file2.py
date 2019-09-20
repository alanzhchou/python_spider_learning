#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#1.字符串，在Python中字符串表现为一个长字符数组
#输出时，+表示字符串的连接符号，*表示连续操作，即为乘法
#用[a:b]输出对应字段，左闭右开，[a:]表示输出从a字段开始直到结尾
a = "IlovePython"

print(a + "!")
print((a + "\t")*3)
print(a[1:])
print(a[1:5])
print()


#2.python列表
#类似java中的容器的概念
#其中元素可以为多种类型的集合，甚至可以包含列表，即为嵌套
#类似string，切割也可用[a:b]，连接用+，
list1 = [2, 2.5, 'Love', True]
list2 = ['a', 100, False, 3.1415926]

list3 = list1*2
list4 = list1 + list2
list5 = list1[1:3]
list6 = list1[1:]
list7 = list1[3]

listTotal = [list1,list2,list3,list4,list5,list6,list7]
for a in listTotal:
    print(a)
print()


#3.python元组(tuple)，类似于list，但不能二次赋值，相当于只读列表
#用()标识，元素间用，隔开
tuple1 = (3, 3.1415, "Love", False)
tuple2 = (True, "You", 0.926535)

tuple3 = tuple1[2]
tuple4 = tuple1[1:]
tuple5 = tuple1[1:3]
tuple6 = tuple1 * 2
tuple7 = tuple1 + tuple2
'''
在list中可进行赋值，如：list1[1] = 200 #并不会报错
但在tuple中不可直接赋值，如：tuple1[1] = "LoveYou" #会报错
TypeError: 'tuple' object does not support item assignment
'''
tupleTotal = (tuple1, tuple2, tuple3, tuple4, tuple5, tuple6, tuple7)

for b in tupleTotal:
    print(b)
print()

#4.python字典(dictionary): 是除去list外最灵活的内置数据类型
#列表是有序对象的集合，字典是无序对象的集合
#字典中存储数据通过键值对的方式，并不是index的偏移
#字典通过{}标识，储存形式为key:value
dict1 = {}
dict1['one'] = "this is the value of key 'one'"
dict1[2] = "I am the value of key 2"

print(dict1['one'])
print(dict1[2])
print(dict1)
print(dict1.keys())
print(dict1.values())
print()

#5.python数据类型转换
#int(python中与2.x中的long),float,complex(复数类型),str,repr,eval,tuple,list,set,dirct
#frozenset(意为冻结的集合，即转化为不可变的集合)，chr，unichr(Unicode的字符)，
#ord(整数值)，hex(十六进制)，oct(八进制)，python3.X中新增了byte，bytearrays类型

#这里的str和repr都有转化成字符串的意思，其区别如下：
# >>> from datetime import datetime
# >>> now = datetime.now()
# >>> print(str(now)) #2017, 10, 4, 20, 10, 41, 600439
# >>> print(repr(now)) #datetime.datetime(2017, 10, 4, 20, 10, 41, 600439)
#可以看到str单纯只是输出实际展现的字符串，不会将调试的实例，函数等输出，于是结论如下
# str() 的输出追求可读性，输出格式要便于理解，适合用于输出内容到用户终端。
# repr() 的输出追求明确性，除了对象内容，还需要展示出对象的数据类型信息，
# 适合开发和调试阶段使用。
from datetime import datetime
now = datetime.now()
print(str(now))
print(repr(now))
print()

#6.小练习给变量，字符串，元祖，字典赋值
varible1 = 2
string1 = "I LOVE PYTHON"
tuple11 = (2017, "I", "LOVE", "PYTHON")
dict11 = {"name":"AlanChou", "age":20, 2017:"I Learn Python!"}

tupleOut = (varible1, string1, tuple11, dict11)
for c in tupleOut:
    print(c)
print()

#7.python中的所有的数据都是类，可通过type()查看数据的对应的类型
for d in tupleOut:
    print(type(d))
print()

#8.isinstance(意为是否为实例),传入参数为（X，类）
#type()不会认为子类是一种父类类型
#isinstance()会认为子类是一种父类类型。
class A:
    pass
class B(A):
    pass
print(isinstance(A(),A))#True
print(type(A()) == A)#True
print(isinstance(B(),A))#True
print(type(A()) == B)#False
print()