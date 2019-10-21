#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jieba
from jieba.analyse import *

with open('./data/自贸','r',encoding='utf8') as f:
    data = f.read()

fw=open('./result/自贸/extract','w',encoding='utf8')

for keyword, weight in extract_tags(data, topK=100, withWeight=True):
    fw.write('%s %f'%(keyword,weight)+'\n')
    #print('%s %s' % (keyword, weight))
