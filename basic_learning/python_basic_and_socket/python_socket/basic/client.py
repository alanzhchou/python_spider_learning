#/usr/bin/env python3
# -*- coding: utf-8 -*-
from socket import *

serverName = '127.0.0.1'
serverPort = 12000

while 1:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    sentence = input("input a integer to get factor:")
    clientSocket.send(sentence.encode())

    messageGet = clientSocket.recv(1024).decode()
    print("server: ", messageGet,"\n")

    clientSocket.close()