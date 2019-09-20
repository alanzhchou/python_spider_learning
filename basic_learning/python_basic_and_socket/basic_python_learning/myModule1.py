#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#fileName: myModule1.py
#for module: myModule1

def my_print(args):
    print('input: ',args)

if __name__ == '__main__':
    print('模块自己在运行')
else:
    print('被调用时执行')