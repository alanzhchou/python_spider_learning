#/usr/bin/env python3
# -*- coding: utf-8 -*-
print('老师辛苦了，以下测试方法各项都已经完整注释，')
print('执行的方法中默认只保留了读文件,增加数据到最后一行，删除第3行，修改第一行\n其他的测试方法被注释，可取消注释测试\n')

#读取测试文件test.txt
#原始数据为
'''
﻿line 1
line 2
line 3
line 4
line 5
'''

class file_operations(object):
    def __init__(self,file_path,encoding='utf-8'):
        self.__file_path = file_path
        self.__encoding = encoding

    def modify_file(self,file_path,encoding='utf-8'):
        self.__file_path = file_path
        self.__encoding = encoding

    #读取并输出到控制台的函数，可选传入编码方式：默认为：utf-8
    def file_read(self):
        with open(self.__file_path,mode='r',encoding=self.__encoding,errors='ignore') as f:
            lines = f.readlines()
            for line in lines:
                print(line,end='')
            print()
        return lines

    #由人工输入内容追加写入文件结尾，无需直接在方法中传入参数
    def file_append_through_input(self):
        with open(self.__file_path, mode='a', encoding=self.__encoding, errors='ignore') as f:
            x = str(input('输入内容以追加到文件末位：\n'))
            while x=='':
                print('未输入，请再次输入！')
                x = str(input('输入内容以追加到文件末位：\n'))
            f.write(x)
            print('已追加写入成功！')

    #在调用方法时需传入内容参数（默认为空）,之后直接把参数追加写入文件末尾
    def file_append_directly(self,content=''):
        with open(self.__file_path, mode='a', encoding=self.__encoding, errors='ignore') as f:
            f.write(str(content))
            if content == '':
                print('已追加写入成功！但是写入为空啊喂！')
            else:
                print('已追加写入成功！\n')

    #由人工输入内容追加写入文件结尾，按一行一行的方式来追加数据，无需直接在方法中传入参数
    def file_append_lines_through_input(self):
        with open(self.__file_path, mode='a', encoding=self.__encoding, errors='ignore') as f:
            lines = ['\n']
            while True:
                x = input('输入内容以行的形式追加到文件末位：\n')
                if x!='':
                    x = str(x) +'\n'
                    lines.append(x)
                while x == '':
                    print('未输入，请再次输入！')
                    x = input('输入内容以行的形式追加到文件末位：\n')
                    if x != '':
                        x = str(x) +'\n'       
                        lines.append(x)
                out = input('按下enter键继续，输入其他任意值按enter退出：\n')
                if out != '':
                    break
            print(lines)
            f.writelines(lines)
            print('已追加写入成功！')

    #在调用方法时需传入内容参数序列（默认为空的序列）,之后直接把参数一行一行追加写入文件末尾
    def file_append_lines_directly(self,content=[]):
        with open(self.__file_path, mode='a', encoding=self.__encoding, errors='ignore') as f:
            content2 = []
            for line in content:
                content2.append(str(line))
            f.writelines(content2)
            if content2 == '':
                print('已追加写入成功！但是写入为空啊喂！')
            else:
                print('已追加写入成功！\n')

    #调用方法时需传入数据所在的行数，实现将该行数据删除
    def file_del_line(self,row=-1):
        if row<=0:
            pass
        elif row>=1:
            with open(self.__file_path, mode='r', encoding=self.__encoding, errors='ignore') as f:
                lines = f.readlines()
            lines[row-1] = ''
            with open(self.__file_path, mode='w', encoding=self.__encoding, errors='ignore') as f:
                f.writelines(lines)
            print('删除第',row,'行成功')

    # 调用方法时需传入修改后的数据，及修改所在的行数，实现将该行数据修改
    def file_modify_line(self,new_agrs,row=-1):
        if row<=0:
            pass
        elif row>=1:
            with open(self.__file_path, mode='r', encoding=self.__encoding, errors='ignore') as f:
                lines = f.readlines()
            lines[row-1] = str(new_agrs) + '\n'
            with open(self.__file_path, mode='w', encoding=self.__encoding, errors='ignore') as f:
                f.writelines(lines)
            print('修改第',row,'行成功\n')


#传入文件名（缺省参数为编码方式，默认为utf-8）生成实例，之后也可用modify_file方法来修改文件和编码方式
file_test = file_operations('test.txt')
#按行输出文件数据到控制台
file_test.file_read()

#插入数据，可选一个执行
#手动输入将要插入的数据，插入到文件末尾（不换行）
# file_test.file_append_through_input()
# file_test.file_read()

#插入数据，可选一个执行
#直接传入将要插入的数据，插入到文件末尾（不换行）
file_test.file_append_directly('\tin line9 appended')
file_test.file_read()

#插入数据，可选一个执行
#手动输入多行，插入到文件末尾
# file_test.file_append_lines_through_input()
# file_test.file_read()

#插入数据，可选一个执行
#直接传入代表多行的数据的序列，插入到文件末尾
# file_test.file_append_lines_directly(['a','b','c','d'])
# file_test.file_read()

#删除数据
#删除第三行的数据
file_test.file_del_line(3)
file_test.file_read()

#修改数据
#修改第一行的数据
file_test.file_modify_line('a modified line',1)
file_test.file_read()