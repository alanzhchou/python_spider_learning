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
print(b)



#################################################
# 2. linespace

