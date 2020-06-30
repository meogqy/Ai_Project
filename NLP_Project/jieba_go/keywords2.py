#!/usr/bin/env python
# -*- coding: UTF-8 –*-
import os   # 
import jieba  # 中文分词
import jieba.analyse # 关键词提取
import pymysql  #连接数据库
import importlib

def query(sql):
	db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='gov', charset='utf8')  #打开数据库连接
	cursor = db.cursor() #使用cursor()方法获取操作游标 
	cursor.execute(sql)  #使用 fetchone() 方法获取一条数据
	data = cursor.fetchall() #执行SQL查询
	cursor.close() #关闭游标
	db.close() #关闭连接
	return data


	

if __name__ =="__main__":
	data=query("select title from gov_report" )  #使用execute方法执行SQL语句
	print (type(data))
	for i in data:
		print (i)
