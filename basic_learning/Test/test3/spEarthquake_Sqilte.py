#/usr/bin/env python3
#-*- coding: utf-8 -*-

# __author__: ZH-AlanChou
# __time__: 2017/12/4
# __version__: 1.0
from time import ctime
import re
import threading
import requests
from bs4 import BeautifulSoup

import pgSQL
import user_agents
import sqlite3

class earthquakeSp(object):
    def __init__(self):
        self.__agents = user_agents.userAgents()

    def getRandomAgent(self):
        return self.__agents.getRandomAgent()

    def getRandomHeader(self):
        return {'user-agent': self.getRandomAgent()}

    def getOnePage(self,url = 'https://www.emsc-csem.org/Earthquake/?view=1'):
        #添加带随机user-Agent的请求头部，最低程度防止被反爬
        req = requests.get(url, headers=self.getRandomHeader())

        #BeautifulSoup解析返回的html文档
        soup = BeautifulSoup(req.text, "lxml")

        #这里两个class分别代表网页中交替颜色的两种行,(normal)|(bold)|(info)代表三种地震等级表示的字体颜色：普通，加粗，红色
        result = soup.find_all("tr", {"class": re.compile(r'ligne[1-2] (normal)|(bold)|(info)')})

        pageInfo = []

        # 计数，每一页有50行，最后输出应为50
        rowNumber = 0

        for row in result:
            rowNumber += 1

            #在每行下寻找各列
            col = row.find_all("td", {"class": re.compile(r'(tabev[1-6])|(tb_region)')})

            earthquakeInfo = []

            #用选取的第几块来过滤少数不相关的内容,每次遍历加一
            blockNumber = 0
            for content in col:
                if blockNumber != 0 and blockNumber != 6:
                    # print(content.text.strip())
                    earthquakeInfo.append(content.text.strip())
                elif blockNumber == 0:
                    # print(re.sub(r'\s\s\s', '-', content.find("a").text))
                    earthquakeInfo.append(re.sub(r'\s\s\s', ' ', content.find("a").text))
                else:
                    pass    # 这里打印的是地震的类型，M，mb等，了解访问 https://tieba.baidu.com/p/853573901
                blockNumber += 1

            #有些莫名奇妙被选进来的空<tr></tr>,防止一下
            if len(earthquakeInfo) != 0:
                # 修改经纬度表示，负纬度表示位于南半球（S）的位置而负经度表示西半球（W）的位置
                if earthquakeInfo[2].upper() == 'S':
                    earthquakeInfo[1] = '-' + earthquakeInfo[1]

                if earthquakeInfo[4].upper() == 'W':
                    earthquakeInfo[3] = '-' + earthquakeInfo[3]

                del earthquakeInfo[2]
                del earthquakeInfo[3]

                pageInfo.append(tuple(earthquakeInfo))
            # print(tuple(earthquakeInfo))

        #返回是否正确爬取，和元组一张页面的信息元组，其中包括各行信息的元组
        return len(pageInfo)==50 or len(pageInfo)==51,tuple(pageInfo)

    def getPagesToIndex(self,index = 1):
        pages = []

        for i in range(1,index+1):
            url = 'https://www.emsc-csem.org/Earthquake/?view=' + str(i)
            resultPage = self.getOnePage(url=url)
            if resultPage[0] == True:
                # for row in resultPage[1]:
                #     print(row)
                pages.append(resultPage[1])
            else:
                break
        return tuple(pages)

    def getPagesFromToIndex(self,begin = 1,end = 2):
        pages = []

        for i in range(begin,end+1):
            url = 'https://www.emsc-csem.org/Earthquake/?view=' + str(i)
            resultPage = self.getOnePage(url=url)
            if resultPage[0] == True:
                # for row in resultPage[1]:
                #     print(row)
                pages.append(resultPage[1])
            else:
                break
        return tuple(pages)

def InsertOnePage(pg,page):
    for row in page:
        # 生成SQL
        sql = 'select auto_insert(\'%s\',%s,%s,%s,%s,\'%s\');'%(row[0],row[1],row[2],row[3],row[4],row[5])
        pg.exeOneOp(sql=sql)

def forTheadings(startIndex,endIndex):
    earthquake = earthquakeSp()

    # 连接数据库
    pg = pgSQL.ToPgSQL(host='39.108.56.218',port='5432',dbname='earthquakedb',user='earthquake',password='earthquake@123')

    startIndex = startIndex
    endIndex = endIndex
    pageNumber = endIndex - startIndex + 1

    while True:
        print(startIndex, '*****', endIndex)
        pages = earthquake.getPagesFromToIndex(begin=startIndex, end=endIndex)

        if len(pages) == 0:
            continue

        for page in pages:
            InsertOnePage(pg,page)

        rowNumber = int(pg.exeOneQuery(sql='select max(id) from quakes;')[0][0])

        startIndex = startIndex + int((rowNumber - 1 - 50) / 51 + 1)

        if rowNumber >= (pageNumber - 1) * 51 or startIndex > endIndex:
            break
    pg.close()

def TheadingsSp(pagesNumber):
    print("%s" % ctime())
    threads = []
    for i in range(1,pagesNumber+1,5):
        t = threading.Thread(target=forTheadings, args=(i, i+4))
        threads.append(t)

    for t in threads:
        t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()
    print("%s" % ctime())

# TheadingsSp(5)


