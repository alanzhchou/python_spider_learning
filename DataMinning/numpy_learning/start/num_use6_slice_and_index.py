#!/usr/env/bin python3
import numpy as np

########################################33
# # slice 切片
# # slice(start,stop,step)
# a = np.empty((6,2),dtype=np.int16)
# print(a,end='\n\n')
#
# # 只传入一个参数返回对应索引,多维数组依次遍历
# print(a[0][1],end='\n\n')
#
# # 一个参数加: 返回对应索引之后的所有
# print(a[5:],end='\n\n')
#
# # 两个参数中间加: 返回对应索引之间的所有
# print(a[3:5],end='\n\n')
#
# # 三个参数中间加: 按步长返回对应索引之间的所有
# print(a[3:5:2],end='\n\n')

###########################################

# 切片还可以包括省略号(...)，来使选择元组的长度与数组的维度相同。
# 如果在行位置使用省略号，它将返回包含行中元素的ndarray。
b = np.empty((3,3),dtype=np.int16)
print(b,end='\n\n')

print(b[...,1])
print(b[1,...])

# 遍历第二列及后续的所有列
print(b[...,1:])
