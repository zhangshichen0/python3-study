#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('food.db')
curs = conn.cursor()

query_sql = 'select * from food'
curs.execute(query_sql)

# print(curs.description) 输出的是字段
# print(curs.fetchall()) 从curs中获取执行sql后的结果

fields = [f[0] for f in curs.description]

for row in curs.fetchall():
    for pair in zip(fields, row):
        print('%s:%s' % pair)
    print()

curs.close()
conn.close()