#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyhanlp import *

#print(HanLP.segment('你好，欢迎在Python中调用HanLP的API'))
#for term in HanLP.segment('下雨天地面积水'):
#print('{}\t{}'.format(term.word, term.nature)) # 获取单词与词性

# 关键词提取

f=open('./data/科创','r',encoding='utf8')
corpus=f.read()
#print(corpus)

print(HanLP.extractKeyword(corpus, 50))
# 自动摘要
#print(HanLP.extractSummary(document, 3))

