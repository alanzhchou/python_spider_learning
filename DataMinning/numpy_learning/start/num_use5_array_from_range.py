#!/usr/env/bin python3
import numpy as np

################################################
# 1. arange生成范围内数组
# numpy.arange(start, stop, step, dtype)
# 1. 	start 范围的起始值，默认为0
# 2. 	stop 范围的终止值(不包含)
# 3. 	step 两个值的间隔，默认为1
# 4. 	dtype 返回ndarray的数据类型，如果没有提供，则会使用输入数据的类型。

a = np.arange(5,dtype=np.float32)
print(a)

b = np.arange(5,20,3,np.float16)
print(b,end='\n\n')



#################################################
# 2. linespace 与 arange 类似指定范围内的均匀间隔数
# numpy.linspace(start, stop, num, endpoint, retstep, dtype)
# 1. 	start 序列的起始值
# 2. 	stop 序列的终止值，如果endpoint为true，该值包含于序列中
# 3. 	num 要生成的等间隔样例数量，默认为50
# 4. 	endpoint 序列中是否包含stop值，默认为ture
# 5. 	retstep 如果为true，返回样例，以及连续数字之间的步长
# 6. 	dtype 输出ndarray的数据类型

c = np.linspace(-10,90,25,dtype=np.float16)
print(c,end='\n\n')

###################################################
# 3. logspace 在对数刻度上均匀分布的数组
# numpy.logscale(start, stop, num, endpoint, base, dtype)
#
# 1. 	start 起始值是base ** start
# 2. 	stop 终止值是base ** stop
# 3. 	num 范围内的数值数量，默认为50
# 4. 	endpoint 如果为true，终止值包含在输出数组当中
# 5. 	base 对数空间的底数，默认为10
# 6. 	dtype 输出数组的数据类型，如果没有提供，则取决于其它参数

d = np.logspace(1,10,num=10,base=2,dtype=np.int16)
print(d,end='\n\n')







