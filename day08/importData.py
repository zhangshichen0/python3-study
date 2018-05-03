#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
使用sqllite数据库，展示简单的数据库操作
~01001~^~0100~^~Butter, salted~^~BUTTER,WITH SALT~^^^~Y~^^0^^6.38^4.27^8.79^3.87

数值之间使用^隔开，值以~开头
'''
import sqlite3


def convert(value):
    '''
    转换内容中数值
    :param value:
    :return:
    '''
    if value.startswith('~'):
        return value.strip('~')
    if not value:
        return 0;
    else:
        return float(value)


conn = sqlite3.connect('food.db')
curs = conn.cursor()

try:
    curs.execute('''
        CREATE TABLE food(
        id VARCHAR(20) primary key,
        desc VARCHAR(20),
        water FLOAT
        )
    ''')
except (sqlite3.OperationalError) as e:
    print(e)


query = 'insert into food values (?,?,?)'

for line in open("food.txt"):
    fields = line.split('^')
    print(len(fields))
    vals = [convert(f) for f in fields[:len(fields)]]
    print(vals)
    curs.executemany(query, [vals]) #注意此处，参数类型为序列

conn.commit()
conn.close()