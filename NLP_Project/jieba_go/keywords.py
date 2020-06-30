#!/usr/bin/env python
# -*- coding: UTF-8 –*-
import os   # 
import jieba  # 中文分词
import jieba.analyse # 关键词提取


# 遍历文件夹
def walkFile(file):
    for root, dirs, files in os.walk(file):

        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list

        # 遍历文件
        for f in files:
          print(os.path.join(root, f))
def main():
    walkFile("C:/Users/yeqigang/OneDrive/python_go/jieba_go/govReports/")


print ("2007政府工作报告_温家宝")
data = open('file','r', encoding='UTF-8')
str = data.read()
content = str
keywords = jieba.analyse.extract_tags(content, topK=20, withWeight=True, allowPOS=())
# 访问提取结果
for item in keywords:
    # 分别为关键词和相应的权重
    print (item[0], item[1])
	
if __name__ == '__main__':
    main()