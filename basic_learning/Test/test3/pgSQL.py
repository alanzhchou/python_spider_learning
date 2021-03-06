#/usr/bin/env python3
#-*- coding: utf-8 -*-

# __author__: ZH-AlanChou
# __time__: 2017/12/5
# __version__: 1.0

import psycopg2

class ToPgSQL(object):
    def __init__(self,host='',port='',dbname='',user='',password=''):
        self.__connInfo = "host=" + host + " port=" + port + " dbname=" + dbname + " user=" + user + " password=" + password
        # 确定页面行信息数，用于之后核对数据库执行插入
        self.__conn = psycopg2.connect(self.__connInfo)

    def tryConnect(self):
        try:
            conn = self.__conn
            cur = conn.cursor()

            str = 'select version()'
            cur.execute(str)
            print(cur.fetchone())
            cur.close()
        except psycopg2.DatabaseError as e:
            print("Connect Error")
            self.__conn = psycopg2.connect(self.__connInfo)

    def exeOneQuery(self,sql=''):
        try:
            conn = self.__conn
            cur = conn.cursor()

            cur.execute(sql)
            result = cur.fetchall()

            cur.close()
            return result
        except psycopg2.DatabaseError as e:
            print("Connect Error")
            self.__conn = psycopg2.connect(self.__connInfo)

    def exeOneOp(self,sql=''):
        try:
            conn = self.__conn
            cur = conn.cursor()

            cur.execute(sql)

            cur.close()
            conn.commit()
        except psycopg2.DatabaseError as e:
            print(sql)
            self.__conn = psycopg2.connect(self.__connInfo)

    def close(self):
        self.__conn.close()



