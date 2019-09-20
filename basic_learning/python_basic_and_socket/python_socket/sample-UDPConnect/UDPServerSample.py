#/usr/bin/env python3
# -*- coding: utf-8 -*-
from socket import *

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('127.0.0.1',serverPort))
print('The server is ready to receive')

while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    capitalizedSentence = message.decode().upper()
    serverSocket.sendto(capitalizedSentence.encode(), clientAddress)