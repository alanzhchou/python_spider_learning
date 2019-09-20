#/usr/bin/env python3
# -*- coding: utf-8 -*-
from socket import *
from tkinter import *
import threading

#客户端的实现类，返回一个可开启的ChatClient实例，构造方法中可传入缺省的端口参数，默认为12001端口，用start()方法开启
class ChatClient(object):
    # 初始化客户端socket，并添加一个类的线程数组，成功设置后输出"Client set!"
    def __init__(self,clientPort = 12001 ):
        self.serverName = '172.18.5.114'
        self.serverPort = 12000
        self.clientSocket = socket(AF_INET, SOCK_DGRAM)
        self.clientSocket.bind(('127.0.0.1', clientPort))
        self.threadings = []
        print("Client set!")

    # UI线程
    def setUI(self):
        self.window = Tk()
        self.chatWindow = Frame(self.window)
        self.showChat = Text(self.chatWindow)
        self.inputArea = Entry(self.chatWindow)
        self.sendButton = Button(self.chatWindow, text="Send",
                                 command=self.send)
        self.showChat.pack(side=TOP, padx=5)
        self.sendButton.pack(side=RIGHT)
        self.inputArea.pack(side=RIGHT, pady=10.0)
        self.chatWindow.pack(side=TOP, padx=5)
        self.window.title("Client GUI for ChatPy")
        self.window.geometry("300x450")
        self.window.resizable(width=True, height=True)
        self.window.mainloop()

    # 实现对GUI中的Text内容的插入，name指定内容的所有者，message指定插入内容
    def insertTo(self,name,message):
        self.showChat.insert("end", name+": "+message+"\n")

    # send动作，检查Entry的内容是否为空，为true的话，向服务端发送消息，并填写本地聊天框
    def send(self):
        sendMessage = self.inputArea.get()
        if sendMessage != "":
            self.insertTo("Client",sendMessage)
            print("发过去惹")
            self.clientSocket.sendto(sendMessage.encode(),(self.serverName, self.serverPort))
        else:
            print("别发空的哦，亲！")

    # 接收消息线程，填写客户端聊天框
    def receive(self):
        while True:
            message, serverAddr = self.clientSocket.recvfrom(2048)
            print("收到服务器传来的惹！")
            getMessage = message.decode()
            self.insertTo("Server",getMessage)

    # 设置接收及本地UI线程，并设置线程守护及拥塞，生成实例后调用该方法，即开启各线程
    def start(self):
        # sendThread = threading.Thread(target=self.send, args="")
        # self.threadings.append(sendThread)
        receiveThread = threading.Thread(target=self.receive, args="")
        self.threadings.append(receiveThread)
        UIThread = threading.Thread(target=self.setUI, args="")
        self.threadings.append(UIThread)

        for t in self.threadings:
            t.setDaemon(True)
            t.start()

        for t in self.threadings:
            t.join()

#生成客户端实例，开启多线程
client = ChatClient()
client.start()