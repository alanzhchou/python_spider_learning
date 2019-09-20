#/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
此类用来测试可滚动的如，listbox和scrollbar等
'''

from tkinter import *

window = Tk()
window.title("My Python GUI")
window.geometry("300x550")
window.resizable(width=True,height=True)

testScrollbar = Frame(window)

t = Text(testScrollbar)
t.insert("end","end\n")
for i in range(1,10):
    t.insert(1.0,'0123456789\n')
t.pack(side = TOP,pady = 8)


def print_item(event):
    print(lb.get(lb.curselection()))


var = StringVar()
lb = Listbox(testScrollbar,listvariable = var)
list_item = [1,2,3,4,5,6,7,8,9,0]


for item in list_item:
    lb.insert(END,item)

# lb.delete(2,4)
# var.set(('a','b','c','d'))
# print(var.get())
lb.bind('<ButtonRelease-1>',print_item)
#将print_item方法绑定给lb


scrl = Scrollbar(testScrollbar)
scrl.pack(side = RIGHT,fill = "y")
lb.configure(yscrollcommand = scrl.set)
lb.pack(side = TOP,fill=BOTH)
scrl['command'] = lb.yview

testScrollbar.pack()
window.mainloop()