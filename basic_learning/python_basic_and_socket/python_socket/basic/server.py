#/usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import *

def factor(a):
    if a<0:
        return "factor error!"
    elif a == 0:
        return 1
    else:
        result = 1
        while a != 0:
            result *= a
            a-=1
        return result

serverPort = 12000

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('127.0.0.1',serverPort))

serverSocket.listen(1)

print("server is listening:")

while 1:
    connectionSocket, addr = serverSocket.accept()

    sentence = int(connectionSocket.recv(1024))

    message = factor(sentence)

    connectionSocket.send(str(message).encode())

    connectionSocket.close()


