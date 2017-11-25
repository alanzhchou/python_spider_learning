#/usr/bin/env python3
# -*- coding: utf-8 -*-

# Socket,建立TCP连接实现Web功能，获取服务器响应，
# 若响应正确（存在文件）则返回成html格式，响应错误（不存在文件）则返回404.html
from socket import *

#判断是否为html文件的函数，输入文件名，是.html文件返回true，不是则返回false
def isHtml(file_name):
    arr = file_name.split('.')
    postfix = arr[len(arr)-1]
    if postfix == "html":
        return True
    else:
        return False

#读取文件，并反馈IOExpection，根据后缀名（是否为html），对读取文件进行不同程度修饰
def file_read(path, encode="utf-8"):
    if path[:1] == '/':
        path = path[1:]

    result = ""
    with open(path, mode='r', encoding=encode, errors='ignore') as f:
        lines = f.readlines()
        for line in lines:
            result += line;

    if isHtml(path):
        result = "HTTP/1.1 200 OK\r\n\r\n" + result
    else:
        result = "HTTP/1.1 200 OK\r\n\r\n" \
                 + "<html><meta charset=\"utf-8\">" \
                 + "<title>" + path + "(格式化为html)" +  "</title>" \
                 + "<body><h1>" + path + "</h1><p>" \
                 + result + "</p></body></html>"
    return result

#建立serverSocket并绑定到本机（127.0.0.1）的80端口，开启一个监听
#（在主机已占用80端口的情况下，请换端口开启）
#开启后由于http响应默认为80端口，则用户无需再输入端口
serverPort = 80
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('127.0.0.1',serverPort))
serverSocket.listen(1)

#主循环监听，并提供服务
while True:
    #测试启动正常，开始服务
    print('Ready to serve...')

    #由响应建立TCP连接
    client_connection, client_address = serverSocket.accept()

    #接受响应报文，解码成str
    request = client_connection.recv(1024).decode()

    #处理响应报文，拿到请求文件路径（含文件名）
    path = request.split('\r')[0].split(' ')[1]

    #尝试在服务器上寻找，路径表示的文件，有则读取并返回该文件，无则返回404页面
    try:
        response = file_read(path)
        print("\tfrom",client_address,"\tGET:",path,", request succeed!")
    except IOError:
        response = file_read("404.html")
        print("\tfrom",client_address,"\tGET:",path,", request fail!")

    #根据读取结果发送响应报文
    client_connection.sendto(response.encode("utf-8"),client_address)

    #关闭TCP连接
    client_connection.close()

