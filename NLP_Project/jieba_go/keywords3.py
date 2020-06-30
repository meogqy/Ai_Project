#!/usr/bin/python
# -*- coding: UTF-8 -*-
import jieba  # 中文分词
import jieba.analyse # 关键词提取
import pymysql  #连接数据库
from pymysql.cursors import DictCursor
# 打开数据库连接
db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='gov', charset='utf8')

# 使用cursor()方法获取操作游标 
cursor = db.cursor(DictCursor)

# 使用execute方法执行SQL语句
sql="select title from gov_report"

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()

for content in data:
	print (type(content))
# 关闭数据库连接
db.close()

keywords = jieba.analyse.extract_tags(content, topK=20, withWeight=True,allowPOS=())
# 访问提取结果
for item in keywords:
    #分别为关键词和相应的权重
     print (item[0], item[1])

