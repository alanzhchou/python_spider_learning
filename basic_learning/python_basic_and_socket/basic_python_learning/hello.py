#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('hello,world!')

a=1
b=1
for c in range(101):
    b=b*(10000-c)
    print(10000-c)
print(b)

for m in range(1000):
    for d in range(101):
        a=a*(10000-d-m)
    print(a)
    if a/b<=0.1:
        print(m)
        break
    a=1