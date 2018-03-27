#!/usr/env/bin python3
import numpy as np

#########################################
# 1. empty返回一定大小的随机初始化数组
a = np.empty((2,3), dtype=np.int16,order='C')
print(a)
print(a.dtype,end='\n\n')

# 2. zeros 返回初始化为 0 的指定大小的数组,这里的dtype指定每个item的格式，这里为（x，y）的格式，但其中的最小单元依然为0
b = np.zeros((4,2), dtype=[('x',np.int16),('y',np.int8)])
print(b)
print(b['x'].dtype, b['y'].dtype ,end='\n\n')

# 3. ones 返回初始化成1的指定大小的数组
c = np.ones((3,2),dtype=[('x',np.int16),('y',np.int8)])
print(c)
print(c['x'].dtype, c['y'].dtype ,end='\n\n')


############################################
# 4. asarray将python的序列和元祖数据类型转化为ndarray，
# 并可指定成特定的存储结构
# list1 = [1,2,3,4,5,6]
# l1 = np.asarray(list1)
# l2 = np.asarray(list1,dtype=[('x',np.float32),('y',np.float32)])
# print(l1)
# print(l2,end='\n\n')


##############################################
# # 5. frombuffer将从缓冲区取得输入生成数组
# # numpy.frombuffer(buffer, dtype = float, count = -1, offset = 0)
# # 1. 	buffer 任何暴露缓冲区借口的对象
# # 2. 	dtype 返回数组的数据类型，默认为float
# # 3. 	count 需要读取的数据数量，默认为-1，读取所有数据
# # 4. 	offset 需要读取的起始位置，默认为0
# s = b'Hello numPy!!!'
# bytes_array = np.frombuffer(s,dtype='S1')
# print(bytes_array)
# ### 这种生成array的方法在 python3 中由于默认字符为unicode，
# # 故此方法只对字节串存在作用，直接输入字符串时会报错
# ## 另外此用法用处太少，更直接高效地是将string化成list输入 np,array
#
# s2 = s.decode()
# print(s2)
# string_array = np.array(list(s2))
# print(string_array)


########################################################
# 6. fromiter从可迭代对象中生成ndarray
# numpy.fromiter(iterable, dtype, count = -1)
# 1. 	iterable 任何可迭代对象
# 2. 	dtype 返回数组的数据类型
# 3. 	count 需要读取的数据数量，默认为-1，读取所有数据

list = range(5)
it = iter(list)
# 使用迭代器创建 ndarray
x = np.fromiter(it, dtype=np.float32, count=3)
print(x)




