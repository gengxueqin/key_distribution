#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
根据词性进行相似句子合并
结巴词性表：
n名词
nr人名
ns地名
nt机构团体
nz其他专名
v动词
vd副动词
vn名动词

'''
import os
import jieba.posseg as pseg


fw = open('./seg/科创/词性','w',encoding='utf8')

fn = open('./data/科创','r',encoding='utf8') # 打开文件
string_data = fn.readlines() # 读出整个文件

for l in string_data:
    # 文本分词
    seg_list = pseg.cut(l) # 分词

    for w in seg_list:
        #print(w.word,w.flag)
        if w.flag in ['n','vd','vn','vi','s']:
            fw.write(w.word+w.flag+' ')
    fw.write('\n')