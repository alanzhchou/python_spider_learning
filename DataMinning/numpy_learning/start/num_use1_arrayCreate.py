#!/usr/env/bin python3
import numpy as np

# 1. N-dimension-array对象，用于构造一个n维的矩阵对象
# 标准构造函数如下：
# numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
# 1. 	object 任何暴露数组接口方法的对象都会返回一个数组或任何(嵌套)序列。
# 2. 	dtype 数组的所需数据类型，可选。
# 3. 	copy 可选，默认为true，对象是否被复制。
# 4. 	order C(按行)、F(按列)或A(任意，默认)。
# 5. 	subok 默认情况下，返回的数组被强制为基类数组。 如果为true，则返回子类。
# 6. 	ndimin 指定返回数组的最小维数。少于指定的最小维度，会被强制转为高维矩阵

a = np.array([100,200,300])
b = np.array([100,200,300],ndmin=2,dtype=complex)
c = np.array([[1, 2, 3], [2, 3, 4]])

print(a,'\n',b,'\n',c)







