#/usr/bin/env python3
# coding: utf-8 -*-
import psycopg2
# python操作postgresql数组

try:
    conn = psycopg2.connect("host=10.20.23.25 port=5432 dbname=cs307 user=u11510629 password=11510629")
    cur = conn.cursor()
    cur.execute('SELECT version()')
    ver = cur.fetchone()
    print(ver,'\n')
    cur.execute("select * from movies;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    conn.close()

except psycopg2.DatabaseError as e:
    print("Connect Error")