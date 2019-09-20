#/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
此类用来测试frame和label等的pack的布局
'''
from tkinter import *

window = Tk()
window.title("My Python GUI")
window.geometry("200x200")
window.resizable(width=True,height=True)

Label(window, text = "the first Label,\n here is the frame",
      bg = "greenyellow", font = ("Arial", 12)).pack(side = TOP,pady = 20)

frm = Frame(window)

frm_L = Frame(frm)
Label(frm_L,text="左上",bg="pink",
      font=("Arial",12)).pack(side=LEFT, ipadx = 5, ipady = 5)
Label(frm_L,text="右上",bg="green",
      font=("Arial",12)).pack(side=RIGHT, ipadx = 5, ipady = 5)
frm_L.pack(side=TOP)

frm_R = Frame(frm)
Label(frm_R,text="左下",bg="yellow",
      font=("Arial",12)).pack(side=LEFT, ipadx = 5, ipady = 5)
Label(frm_R,text="右下",bg="purple",
      font=("Arial",12)).pack(side=RIGHT, ipadx = 5, ipady = 5)
frm_R.pack(side=TOP)

frm.pack(pady = 5)



window.mainloop()













# x = 360
# y = 160
# top = y - 30
# bottom = y - 30
#
# canvas = Canvas(width=400, height=600, bg='white')
# for i in range(20):
#     canvas.create_oval(250 - top, 250 - bottom, 250 + top, 250 + bottom)
#     top -= 5
#     bottom += 5
# canvas.pack()
# mainloop()
