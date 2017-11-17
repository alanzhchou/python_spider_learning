#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import psycopg2
import requestUseReg


class SimpleSpider(object):
    def __init__(self,host,port,dbname,user,passwd):
        self.__host = host
        self.__port = port
        self.__dbname = dbname
        self.__user = user
        self.__passwd = passwd

    def __errorAtConnection(self):
        print("can not connect to the database")

    def __errorDuringUse(self):
        print("error in connect period")

    def getAConnection(self):
        try:
            connection = psycopg2.connect(host=self.__host,port=self.__port,dbname=self.__dbname,user=self.__user,password=self.__passwd)
            return connection
        except psycopg2.DatabaseError as e:
            self.__errorAtConnection()

    def test_connect(self):
        self.directExcuteSingle("select version();")
        self.directExcuteSingle("select tablename from pg_tables where schemaname='public';")

    def directExcuteSingle(self,command):
        try:
            conn = self.getAConnection()
            cur = conn.cursor()
            cur.execute(command)
            for row in cur.fetchall():
                print(row)
            conn.close()
        except psycopg2.DatabaseError as e:
            self.__errorDuringUse()

    def directExcuteMany(self,command,info):
        try:
            conn = self.getAConnection()
            cur = conn.cursor()
            cur.executemany(command,info)
            conn.commit()
            conn.close()
        except psycopg2.DatabaseError as e:
            self.__errorDuringUse()

simple = SimpleSpider('39.108.56.218','5432','spider','pythonsp','pythonsp@123')
# simple.test_connect()

info = requestUseReg.RequestReg().getInfo()

str1 = "insert into spider_test (first_name,last_name) VALUES (%s,%s);"
simple.directExcuteMany(str1,info)

simple.directExcuteSingle("select * from spider_test ORDER by id;")










