#/usr/bin/env python3
# -*- coding: utf-8 -*-
from socket import *

class client(object):
    def __init__(self):
        self.serverName = '127.0.0.1'
        self.serverPort = 12000
        self.clientSocket = socket(AF_INET, SOCK_DGRAM)

    def send(self):
        sentence = input('Input lowercase sentence:').encode()
        self.clientSocket.sendto(sentence, (self.serverName, self.serverPort))

    def receive(self):
        modifiedSentence, serverAddress = self.clientSocket.recvfrom(2048)
        print(modifiedSentence.decode())
        self.clientSocket.close()

a = client()
while True:
    a.send()
    a.receive()