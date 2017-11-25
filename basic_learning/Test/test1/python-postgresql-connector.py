#!/usr/bin/env python3
# coding: utf-8 -*-
import random
import psycopg2
import requests
# python操作postgresql数组

#测试用的随机列表
# repo = ['Audi','Mercedes',
    #         'Mercedes','Skoda',
    #         'Skoda','Volvo',
    #         'Bentley','Volkswagen',
    #         'Citroen', 'Hummer']
    #
    # info = []
    # for i in range(5):
    #     temp = []
    #     temp.append(repo[random.randint(1,9)])
    #     temp.append(repo[random.randint(1, 9)])
    #     temp = tuple(temp)
    #     info.append(temp)
    # info = tuple(info)

url = 'https://github.com/timeline.json'
response1 = requests.get(url)
header = response1.headers

info = []
for headerItem in header:
    temp = []
    temp.append(headerItem)
    if len(header.get(headerItem)) < 40:
        temp.append(header.get(headerItem))
    else:
        temp.append('too long')
    info.append(tuple(temp))
info = tuple(info)

try:
    conn = psycopg2.connect("host=39.108.56.218 port=5432 dbname=spider user=pythonsp password=pythonsp@123")
    cur = conn.cursor()

    str1 = "insert into spider_test (first_name,last_name) VALUES (%s,%s);"
    cur.executemany(str1,info)
    cur.close()
    conn.commit()

    cur.execute("select * from public.spider_test;")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    conn.close()

except psycopg2.DatabaseError as e:
    print("Connect Error")