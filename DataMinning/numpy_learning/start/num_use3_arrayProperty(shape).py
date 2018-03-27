#!/usr/env/bin python3
import numpy as np

# shape返回矩阵的大小
a = np.array([[1,2,3],[4,5,6]])
print(a)
print(a.shape)
print()

# 通过shape 和 reshape 使数列再次按照指定维数矩阵化
a.shape = (3,2)
print(a)
a = a.reshape(2,3)
print(a)
print()

#########################################
# ndim 返回数组维度
b = np.arange(24)
print(b.ndim)
b.shape = (2,3,4)
print(b.ndim)
print()

#########################################3
# itemsize返回单元素的储存长度，以字节计算
c = np.array([[1,2,3,4],[5,6,7,8]],dtype=np.int16)
print(c.itemsize)
# item按数组形式返回对应值，下标从零开始
c.item(5)
# itemset设置某一个item的值，第一个参数可以为数组形式的index，也可以为元祖形式指定的位置（下标以0开始）
c.itemset(4,25)
print(c)
print()

#flags 可以返回当前数组存储结构的信息
print(c.flags)

# 1. 	C_CONTIGUOUS (C) 数组位于单一的、C 风格的连续区段内
# 2. 	F_CONTIGUOUS (F) 数组位于单一的、Fortran 风格的连续区段内
# 3. 	OWNDATA (O) 数组的内存从其它对象处借用
# 4. 	WRITEABLE (W) 数据区域可写入。 将它设置为flase会锁定数据，使其只读
# 5. 	ALIGNED (A) 数据和任何元素会为硬件适当对齐
# 6. 	UPDATEIFCOPY (U) 这个数组是另一数组的副本。当这个数组释放时，
# 源数组会由这个数组中的元素更新