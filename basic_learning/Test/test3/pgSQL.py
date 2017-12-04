#/usr/bin/env python3
#-*- coding: utf-8 -*-

# __author__: ZH-AlanChou
# __time__: 2017/12/5
# __version__: 1.0

import psycopg2

class ToPgSQL(object):
    def __init__(self,host='',port='',dbname='',user='',password=''):
        self.__connInfo = "host=" + host + " port=" + port + " dbname=" + dbname + " user=" + user + " password=" + password

    def getConnection(self):
        return psycopg2.connect(self.__connInfo)

    def tryConnect(self):
        try:
            conn = self.getConnection()
            cur = conn.cursor()

            str = 'select version()'
            cur.execute(str)
            print(cur.fetchone())
            cur.close()

            # cur = conn.cursor()
            # cur.execute("select * from PUBLIC.plates;")
            # rows = cur.fetchall()
            # for row in rows:
            #     print(row)
            # cur.close()

            conn.close()
        except psycopg2.DatabaseError as e:
            print("Connect Error")

    # def


