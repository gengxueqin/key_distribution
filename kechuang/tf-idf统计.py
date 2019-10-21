# encoding=utf-8
import codecs
import os

import jieba.analyse
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


corpus = []
for i in open('./seg/自贸/分词','r',encoding='utf8').readlines():
    corpus.append(i.strip('\n'))
#print(corpus)
title = []
for txt in os.listdir('./data/2'):
    title.append('\n'+txt.split(".")[0]+'\n\t')

tfidf_model = TfidfVectorizer()
tfidf_matrix = tfidf_model.fit_transform(corpus)
word_dict=tfidf_model.get_feature_names()
feature_dict = {v: k for k, v in tfidf_model.vocabulary_.items()}  # index -> feature_name
top_n_matrix = np.argsort(-tfidf_matrix.todense())[:, :100]  # top tf-idf words for each row
df = pd.DataFrame(np.vectorize(feature_dict.get)(top_n_matrix), index=title)  # convert matrix to df
#print(word_dict)
#print(tfidf_matrix)

df.to_csv("./result/自贸/tf-idf.txt", header=False, encoding='utf-8')