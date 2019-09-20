#/usr/bin/env python3
# -*- coding: utf-8 -*-
from socket import *
from tkinter import *
import threading

#服务器端的实现类，返回一个可开启的ChatServer实例，构造方法中可传入缺省的端口参数，默认为12000端口，用start()方法开启
class ChatServer(object):
    #初始化服务器端socket，并添加一个类的线程数组，成功设置后输出"Server set!"
    def __init__(self,serverPort = 12000):
        self.serverSocket = socket(AF_INET, SOCK_DGRAM)
        self.serverSocket.bind(('127.0.0.1', serverPort))
        self.clientAddr = ()

        self.threadings = []
        print("Server set!")

    #UI线程
    def setUI(self):
        self.window = Tk()
        self.chatWindow = Frame(self.window)
        self.showChat = Text(self.chatWindow)
        self.inputArea = Entry(self.chatWindow)
        self.sendButton = Button(self.chatWindow, text="Send"
                                 ,command=self.send)
        self.showChat.pack(side=TOP, padx=5)
        self.sendButton.pack(side=RIGHT)
        self.inputArea.pack(side=RIGHT, pady=10.0)
        self.chatWindow.pack(side=TOP, padx=5)
        self.window.title("Server GUI for ChatPy")
        self.window.geometry("300x450")
        self.window.resizable(width=True, height=True)
        self.window.mainloop()

    #实现对GUI中的Text内容的插入，name指定内容的所有者，message指定插入内容
    def insertTo(self,name,message):
        self.showChat.insert("end", name+": "+message+"\n")

    #check是否有客户端连入，有则返回True，否则返回False
    def checkClient(self):
        if self.clientAddr == ():
            return False
        else:
            return True

    #接收消息线程，如果是第一次接收，则填写客户端地址
    def receive(self):
        while True:
            message, clientAddr = self.serverSocket.recvfrom(2048)
            print("收到客户端传来的惹！")
            getMessage = message.decode()
            self.insertTo("Client", getMessage)
            if not self.checkClient():
                self.clientAddr = clientAddr

    #send动作，检查Entry的内容是否为空，以及客户端的地址是否已经填写，都为true的话，向客户端发送消息，并填写本地聊天框
    def send(self):
        sendMessage = self.inputArea.get()
        if sendMessage != "":
            if self.checkClient():
                self.insertTo("Server", sendMessage)
                self.serverSocket.sendto(sendMessage.encode(), self.clientAddr)
                print("发过去惹！")
            else:
                print("你个服务器，没人给你发，你给谁发2333")
        else:
            print("别发空的哦，亲！")

    #设置接收及本地UI线程，并设置线程守护及拥塞，生成实例后调用该方法，即开启各线程
    def start(self):
        # sendThread = threading.Thread(target=self.send, args="")
        # self.threadings.append(sendThread)
        receiveThread = threading.Thread(target=self.receive, args="")
        self.threadings.append(receiveThread)
        UIThread = threading.Thread(target=self.setUI,args="")
        self.threadings.append(UIThread)

        for t in self.threadings:
            t.setDaemon(True)
            t.start()

        for t in self.threadings:
            t.join()

#生成服务端实例，开启多线程
server = ChatServer()
server.start()


