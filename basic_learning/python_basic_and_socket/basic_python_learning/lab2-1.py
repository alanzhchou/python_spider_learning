#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self):
        self.__student = {}
        self.__out = []

    def get_student(self):
        return self.__student

    def get_out(self):
        return self.__out

    def append_student(self,ID,name):
        self.__student[ID] = name

    def ID_to_name(self,ID):
        print(self.__student[ID])
        return self.__student[ID]

    def sort_out(self):
        sorted_keys = sorted(self.__student.keys())
        for a in sorted_keys:
            self.__out.append(self.__student[a])
        print(self.__out)
        return self.__out

class Student15(Student):
    def sort_out(self):
        sorted_keys = sorted(self.get_student().keys())
        for a in sorted_keys:
            self.get_out().append(self.get_student()[a])
        print(self.get_out()[::-1])
        return self.get_out()[::-1]

g15 = Student15()
#添加学生姓名，学号
g15.append_student(11510628,'Jack')
g15.append_student(11510629,'Alan')
g15.append_student(11510630,'Dean')
g15.append_student(11510631,'Alice')
#按学生学号查找姓名
g15.ID_to_name(11510628)
studentItems = g15.get_student()
for item in studentItems.values():
    print(item,end="\t")
print()
#重写输出方法，按学号从大到小输出
g15.sort_out()

