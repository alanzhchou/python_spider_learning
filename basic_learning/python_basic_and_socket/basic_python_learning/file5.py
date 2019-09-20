#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#1.python模块学习
#文件夹:using_sys.py
import sys
#这里输出的是脚本加载和python配置的系统的环境变量，包含python解释器
#自动查询所需模块的路径列表
print('\n\nPython路径为：',sys.path)
#argv输出一个代表程序和外部参数的序列，其中第一个参数是本脚本的路径
print(sys.argv[0])
print()

#即在python中，用import xxxxx来导入模块，
#调用模块中的函数：模块名.函数名


#2.导入我的测试模块
import myModule1
myModule1.my_print('Hello,module!')
#导入模块，python的解析器有特定的搜索的顺序：
#1. 当前的目录
#2. 在系统环境变量的PATHONPATH下遍历每个目录，
#3. 查找默认目录，unix下为、/usr/local/lib/python/

#3.from xxx import xxx
#此语句让我们从模块中导入一个指定的部分到当前的空间中
#如导入模块fib下的fibonacci函数
#from fib import fibonacci
#而如果导入一个模块的所有内容也可以这种形式
#from module import *
#但是那些由单一下划线（_）开头的名字不会被导入，（这种形式不应过多使用）

#一个模块在被另一个程序第一次引入的时候，会执行其的主程序
'''
在导入模块中定义：
if __name__ == '__main__':
    print('模块自己在运行')
else:
    print('被调用时执行')
#模块都有一个__name__属性，当值为__main__时表示自身调用，
否则为其他的程序调用
'''

#4.查看导入模块里定义的变量和函数：dir()函数：
import math
counter = 0;
for i in dir(math):
    print(i,end='\t')
    counter+=1
    if counter%8 ==0:
        print()
print()
print(math.e,'\t',math.pi)
print()

#5.python包（库）
#python中的包是一种管理模块的命名空间的形式
#表示为xxx.yyy
#xxx表示为包，yyy表示包中的某一模块
#以假设的音频文件处理库来展示架构：
'''
sound/#顶层包
    __init__.py     #初始化文件
    formats/        #格式处理包
        __init__.py
        wav.py
        mp3.py
        avi.py
        ...
    effects/        #声音效果包
        __init__.py
        surround.py
        reverser.py
        ...
    filters/        #过滤器包
        eq.py
        ...
'''
#在解释器寻找包是只有含有一个__init__的文件目录会被看做一个包
#如上导入时可以写为如下：
'''
import sound.effects.surround   #导入环绕声模块
#这样在后续使用时会需要用全名才可调用：
sound.effects.surround.surround(input,ouput,level...)

#还可以以另一种方式导入：
from sound.effects import surround
#这样就可以以正常的模块名.方法名来调用
surround.surround(input,ouput,level...)
'''
#这里包中的定义的__init__.py文件存在一个__all__的列表变量
#则在使用from package import*的时候就把该列表中的所有名字作为包内容导入
#如在__init__.py中定义：__all__ = ["echo", "surround", "reverse"]
#则只会导入上述三个子模块，PS，__init__.py文件的__all__的列表变量未定义的
#话，则不会导入任何子模块，此时只可能运行__init__.py里的初始化代码

