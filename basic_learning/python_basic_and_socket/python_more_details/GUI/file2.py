#/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
此模块用来测试文字组件，包括text，entry等
'''

from tkinter import *
import tkinter.messagebox as messagebox

window = Tk()
window.title("My Python GUI")
window.geometry("300x450")
window.resizable(width=True,height=True)

textFrame = Frame(window)

t = Text(textFrame)
t.insert("end","end\n")
for i in range(1,10):
    t.insert(1.0,'0123456789\n')
t.pack(side = TOP,padx = 5)

e = Entry(textFrame)
e.pack(side = TOP,pady = 5.0)

def insertANewLine():
    t.insert(1.0, "a new line\n")

def insertFromEntry():
    a = e.get() + "\n"
    if a != "\n":
        t.insert("end", e.get()+"\n")

Button(textFrame, text ="press for insert a new line",
       command = insertANewLine).pack()

Button(textFrame, text ="press for insert the entrytext to the end",
       command = insertFromEntry).pack()

textFrame.pack(side = TOP, padx = 5)

window.mainloop()



# from tkinter import *
# import tkinter.messagebox as messagebox
#
# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()
#
#     def createWidgets(self):
#         self.nameInput = Entry(self)
#         self.nameInput.pack()
#         self.alertButton = Button(self, text='Hello', command=self.hello)
#         self.alertButton.pack()
#
#     def hello(self):
#         name = self.nameInput.get() or 'world'
#         print(name + "\n")
#         # messagebox.showinfo('Message', 'Hello, %s' % name)
#
# app = Application()
# # 设置窗口标题:
# app.master.title('Hello World')
# # 主消息循环:
# app.mainloop()