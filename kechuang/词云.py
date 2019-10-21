#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re # 正则表达式库
import collections # 词频统计库
import numpy as np # numpy数据处理库
import jieba # 结巴分词
import wordcloud # 词云展示库
from PIL import Image # 图像处理库
import matplotlib.pyplot as plt # 图像展示库

# 读取文件
fn = open('./data/自贸','r',encoding='utf8') # 打开文件
string_data = fn.read() # 读出整个文件
fn.close() # 关闭文件

# 文本预处理
pattern = re.compile(u'\t|\n|\。|，|；|；|\)|\(|\?|"| ') # 定义正则表达式匹配模式
string_data = re.sub(pattern, '', string_data) # 将符合模式的字符去除

# 文本分词
seg_list_exact = jieba.cut(string_data, cut_all = False) # 精确模式分词
stopwords = [line.strip() for line in open('f:/stopwords/stopwords.txt', 'r').readlines()]

object_list=[t for t in seg_list_exact if t not in stopwords]   # 去停


# 词频统计
word_counts = collections.Counter(object_list) # 对分词做词频统计
fw=open('./result/自贸/keyword','w',encoding='utf8')
fw.write(str(word_counts))
word_counts_top10 = word_counts.most_common(10) # 获取前10最高频的词
print (word_counts_top10) # 输出检查

# 词频展示
mask = np.array(Image.open('./timg.jpg')) # 定义词频背景
wc = wordcloud.WordCloud(background_color='white',
    font_path='C:\Windows\Fonts\simhei.ttf',
    mask=mask, # 设置背景图
    max_words=200, # 最多显示词数
    max_font_size=100 # 字体最大值
)

wc.generate_from_frequencies(word_counts) # 从字典生成词云
image_colors = wordcloud.ImageColorGenerator(mask) # 从背景图建立颜色方案
wc.recolor(color_func=image_colors) # 将词云颜色设置为背景图方案
plt.imshow(wc) # 显示词云
plt.axis('off') # 关闭坐标轴
plt.show() # 显示图像
