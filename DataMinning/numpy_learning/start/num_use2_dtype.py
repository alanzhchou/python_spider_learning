#!/usr/env/bin python3
import numpy as np

# numpy中可用的数据类型，多于python
# 1. 	bool_存储为一个字节的布尔值(真或假)
# 2. 	int_默认整数，相当于 C 的long，通常为int32或int64
# 3. 	intc相当于 C 的int，通常为int32或int64
# 4. 	intp用于索引的整数，相当于 C 的size_t，通常为int32或int64
# 5. 	int8字节(-128 ~ 127)
# 6. 	int1616 位整数(-32768 ~ 32767)
# 7. 	int3232 位整数(-2147483648 ~ 2147483647)
# 8. 	int6464 位整数(-9223372036854775808 ~ 9223372036854775807)
# 9. 	uint88 位无符号整数(0 ~ 255)
# 10. 	uint1616 位无符号整数(0 ~ 65535)
# 11. 	uint3232 位无符号整数(0 ~ 4294967295)
# 12. 	uint6464 位无符号整数(0 ~ 18446744073709551615)
# 13. 	float_float64的简写
# 14. 	float16半精度浮点：符号位，5 位指数，10 位尾数
# 15. 	float32单精度浮点：符号位，8 位指数，23 位尾数
# 16. 	float64双精度浮点：符号位，11 位指数，52 位尾数
# 17. 	complex_complex128的简写
# 18. 	complex64复数，由两个 32 位浮点表示(实部和虚部)
# 19. 	complex128复数，由两个 64 位浮点表示(实部和虚部)


# NumPy 数字类型是dtype(数据类型)对象的实例，
# 每个对象具有唯一的特征。 这些类型可以是np.bool_，np.float32等。

# 对于多维度的矩阵，指定其各分量上的类型（分量名）

# 1. 构造dtype
# numpy.dtype(obj, align=False, copy=False)

# Object：被转换为数据类型的对象。
# Align：如果为true，则向字段添加间隔，使其类似C的结构体。
# Copy? 生成dtype对象的新副本，如果为flase，结果是内建数据类型对象的引用。

# self_test
student = np.dtype([('name',np.str_,20), ('age',np.int), ('marks',np.float)])
studentSet = np.array([('alan', 15, 95.5),('chou', 18, 90.5)],dtype=student)

# 用 fields (返回字典) 输出各列标签
for key in student.fields:
    print(key, ' : ', student.fields[key])

print()

# 用 descr (返回列表) 输出各列标签
for index in student.descr:
    print(index[0],' : ',index[1])

print()

for ele in studentSet['name']:
    print(ele,end='\t')

print()
