#!/usr/bin/env python
# coding:utf8
 
import sys
reload(sys)
sys.setdefaultencoding("utf8")

# 关键词提取
import jieba.analyse
 
# 字符串前面加u表示使用unicode编码
with open("/Users/yeqigang/Desktop/python_go/nlp_data/test.txt", "r") as f:  # 打开文件
    data = f.read()  # 读取文件
    content = data
    

    #content = u'原标题：国家卫健委：康复患者管理后续工作包括疾病、身体功能和心理恢复三方面人民网北京4月21日电（董童）在今日举行的国务院联防联控机制新闻发布会上，国家卫生健康委医政医管局监察专员郭燕红表示，患者治愈出院后，后续还有一系列的管理，主要包括对该患者的隔离医学观察、健康监测、复诊复检、康复管理等几个方面。在该患者进行隔离观察的过程中，首先应该单人居住，注意通风，注意手卫生，同时减少人群聚集。在家人照顾过程中，需要患者和家人都佩戴口罩，同时也要注意给患者加强营养。郭燕红介绍，后续工作主要包括三方面：一是帮助患者有关疾病的恢复；二是有关身体功能的恢复；三是对于心理的恢复。而心理的恢复，与疾病、身体的恢复相比同等重要。在社区内，无论是亲戚、邻居、家人，都要关注、关心和关爱好出院患者。出院患者作为康复期患者，体内已有特异性抗体，使得他能够像正常人一样生活，不会造成感染他人的现象。所以在社区，他们需要更多的关爱。“我们也希望，社区同仁能够接纳康复患者的回归，共同来维护好他们的健康，更重要的是给予他们心理的关爱，让他们能够感受到社会大家庭的温暖。所以心理的康复、心理的疏导也是非常重要的。”郭燕红说。'
 
# 第一个参数：待提取关键词的文本
# 第二个参数：返回关键词的数量，重要性从高到低排序
# 第三个参数：是否同时返回每个关键词的权重
# 第四个参数：词性过滤，为空表示不过滤，若提供则仅返回符合词性要求的关键词
keywords = jieba.analyse.extract_tags(content, topK=50, withWeight=True, allowPOS=())
# 访问提取结果
for item in keywords:
    # 分别为关键词和相应的权重
    print item[0], item[1]
 
# 同样是四个参数，但allowPOS默认为('ns', 'n', 'vn', 'v')
# 即仅提取地名、名词、动名词、动词
keywords = jieba.analyse.textrank(content, topK=50, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v'))
# 访问提取结果
for item in keywords:
    # 分别为关键词和相应的权重
    print item[0], item[1]