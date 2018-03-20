#!/usr/env/bin python3
from pageRank import PageRank

#图连通形式用字典保存，各点存在至少一种不同的标记以区分
graph1 = {
        'a':['b', 'c', 'd'],
        'b':['d', 'e'],
        'c':['e'],
        'd':['e'],
        'e':['a']
    }

#定义矩阵中的排序，即结果放在的位置，如下即代表结果列表的各项数值依次为a,b,c,d,e的极限值
sortArray = ['a','b','c','d','e']

rank = PageRank(graph1, sortArray)
rank.printOriginalRankVector()
rank.cal(30)
# rank.printNowRankVector()