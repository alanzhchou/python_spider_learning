#/usr/bin/env python3
# -*- coding: utf-8 -*-

#author：Alan
#用来计算计算机网络中的包交换网络 n 人在线同时传输的概率
#the formula of this problem based on
#P(n) = [nCN * p^n * (1-p)^(N-n)]
'''
P(n): 该网络中n人同时在线的概率
N：网络中所有的用户数
n：该网络中n人同时在线
p：网络中对于个人的在线概率（即个人的使用时间）
'''

class P_of_networks(object):
    def __init__(self,total,p_person):
        self.__total = total
        self.__p_person = p_person

    def __conbination(self,n,N):
        conbin = 1
        for i in range(n):
            conbin *= (N-i)/(i+1)
        return int(conbin)

    def p_of_n(self,n):
        conbination = self.__conbination(n,self.__total)
        N = self.__total
        p = self.__p_person
        return round(conbination*(p**n)*(1-p)**(N-n),4)

    def p_more_than_n(self,n):
        N = self.__total
        P = 0
        if  n > N/2:
            for persons in range(n,N+1,1):
                P += self.p_of_n(persons)
        else:
            for persons in range(1, n+1, 1):
                P += self.p_of_n(persons)
            P = 1 - P
        return round(P, 4)

x = P_of_networks(120,0.1)
print(x.p_more_than_n(20))








