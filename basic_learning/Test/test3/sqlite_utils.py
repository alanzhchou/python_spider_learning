#/usr/bin/env python3
#-*- coding: utf-8 -*-

import sqlite3

class ToSqlite(object):
    def __init__(self,sqliteFilePath):
        self.__connInfo = sqliteFilePath
        # 确定页面行信息数，用于之后核对数据库执行插入
        try:
            self.__conn = sqlite3.connect(self.__connInfo)
        except sqlite3.DatabaseError:
            print("Connect Error")

    def tryConnect(self):
        try:
            conn = self.__conn
            cur = conn.cursor()
            str = 'SELECT sqlite_version();'
            cur.execute(str)
            print(cur.fetchone())
            cur.close()
        except sqlite3.DatabaseError as e:
            print("Sql Error")
            self.__conn = sqlite3.connect(self.__connInfo)

    def exeOneQuery(self,sql=''):
        try:
            conn = self.__conn
            cur = conn.cursor()

            cur.execute(sql)
            result = cur.fetchall()

            cur.close()
            return result
        except sqlite3.DatabaseError as e:
            print("Sql Error")
            self.__conn = sqlite3.connect(self.__connInfo)

    def exeOneOp(self,sql=''):
        try:
            conn = self.__conn
            cur = conn.cursor()

            cur.execute(sql)

            cur.close()
            conn.commit()
        except sqlite3.DatabaseError as e:
            print(sql)
            self.__conn = sqlite3.connect(self.__connInfo)

    def close(self):
        self.__conn.close()

sqliteMe = ToSqlite('my_earthquakes.sqlite')
sqliteMe.tryConnect()
sqliteMe.close()