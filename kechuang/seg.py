#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
import sys
import pickle
import re
import  codecs
import string
import shutil
from win32com import client as wc
import docx

def doSaveAas():
    word = wc.Dispatch('Word.Application')
    doc = word.Documents.Open(u'E:\code\\xxxx.doc')        # 目标路径下的文件
    doc.SaveAs(u'E:\\code\\hhhhhhhh.docx', 12, False, "", True, "", False, False, False, False)  # 转化后路径下的文件
    doc.Close()
    word.Quit()

doSaveAas()
'''

#  分词
import jieba
import os

#读取原始语料库
def savefile(savepath,content):
    with open(savepath,"w",encoding='utf8',errors='ignore') as fp:
        fp.write(content)

def readfile(path):
    with open(path,"r",encoding='utf8',errors='ignore') as fp:
        content = fp.read()
    return content

#给语料库一份一份地分词、去停止词
def corpus_seg(corpus_path,seg_path):
    catelist=os.listdir(corpus_path)
    for mydir in catelist:
        class_path=corpus_path+mydir+"/"
        seg_dir=seg_path+mydir+"/"

        if not os.path.exists(seg_dir):
            os.makedirs(seg_dir)
        stop = [line.strip() for line in open('f:/stopwords/stopwords.txt','r',encoding='utf8',errors='ignore').readlines()]
        file_list = os.listdir(class_path)
        for file_path in file_list:
            fullname = class_path+file_path
            content = readfile(fullname)

            content=content.replace("\r\n", "")
            content=content.replace(" ", "")
            content_seg=jieba.cut(content)
            seg_t=[t for t in content_seg if t not in stop]   # 去停

            savefile(seg_dir+file_path," ".join(seg_t))  #去停止词
            #savefile(seg_dir + file_path, " ".join(list(content_seg-stop)))  #去停止词
    print("中文语料库分词结束！！！")


if __name__ == "__main__":
    corpus_path = "./data/"
    seg_path = "./seg/"
    corpus_seg(corpus_path, seg_path)
