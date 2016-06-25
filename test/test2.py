# coding:utf-8
# import time
# timestamp = time.time()
# timestamp = str(timestamp)[0:str(timestamp).find('.')]
# print timestamp
# list dict def

# 保留字，运算符，分界符，常数，标识符。
"""
  （1）保留字

  （2）常数：由0-----9这几个数字组成

  （3）标识符：由字母打头的字母和数字的字符串

  （4）运算符：+，-，*，/，:=，>=，<=，#

  （5）分界符：，、.、(、)、{} []；


假若text是单词集合的列表

len(text)  #单词个数

set(text)  #去重

sorted(text) #排序

text.count('a') #数给定的单词的个数

text.index('a') #给定单词首次出现的位置

FreqDist(text) #单词及频率，keys()为单词，*[key]得到值

FreqDist(text).plot(50,cumulative=True) #画累积图

bigrams(text) #所有的相邻二元组

text.collocations() #找文本中频繁相邻二元组

text.concordance("word") #找给定单词出现的位置及上下文

text.similar("word") #找和给定单词语境相似的所有单词

text.common_context("a“,"b") #找两个单词相似的上下文语境

text.dispersion_plot(['a','b','c',...]) #单词在文本中的位置分布比较图

text.generate() #随机产生一段文本

"""
# 把所有类型做成一个列表

# 关键字 keyword.kwlist 常数isdigit()  除去另外四种都是标识符  运算符 分界符（自己定义列表 逐一排查）
# 先把注释提取出来
# 生成列表
# http://wiki.jikexueyuan.com/project/python-language-reference/lexical-analysis.html
import keyword
import nltk

print keyword.kwlist
keywords = keyword.kwlist
text = """

"""
# for t in text.split():
#     print t
# for x in text.split():
#     print keyword.iskeyword(x), x
# for key in keywords:
#     print text.count(key), key


# from nltk.book import *
# print text1
# print nltk.word_tokenize(text)
# nltk.download('punkt')
lsttext = nltk.word_tokenize(text)
for x in lsttext:
    print x
print u'len(lsttext)=', len(lsttext)
print u'去掉列表中重复的元素:', set(lsttext)


