#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

# 打开数据库连接
db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='gov', charset='utf8')

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# 使用execute方法执行SQL语句
sql="select * from gov_report"
cursor.execute(sql)

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()

print (data)

# 关闭数据库连接
db.close()