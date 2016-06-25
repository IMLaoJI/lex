# coding:utf-8
__author__ = '刘亮均'
# 对python源码进行词法分析 ，未完善功能：无法剔除多行注释 如:("""  注释内容 """)
import keyword
import re
import time

filename = 'forwork.py'
keywords = keyword.kwlist
operator = ['+', '-', '*', '/', '<=', '>=', '<', '>', '=', '%', '+=', '-=', '/=', '*=', '&', '|', '//', '<<', '>>']
division = [',', ';', '.', '(', ')', '{', '}', '[', ']', ':', "'", '"']


def get_annotations():
    annotations = []
    with open(filename) as fo:
        line = fo.readlines()
        for p in line:
            if p.find('#') >= 0:
                strings = p[p.find('#'):len(p)]
                annotations.append(strings)
                print u'注释：', strings.decode('utf-8')
    return annotations


def replace_annotations():
    annotation = get_annotations()
    with open(filename) as fo:
        txt = fo.read()
        for x in annotation:
            txt = txt.replace(x, '\n')
    return txt


def get_list():
    word_list = []  # 存储所有词
    blank = re.compile(r"\s")
    texts = replace_annotations()
    ts = re.sub(blank, ' ', texts)  # 用空格符替换所有空白符
    ts = ts.strip()
    lst = list(ts)  # str -> list
    word = []   # 存储单个词
    sign =['-', '=', '+', '<', '>', '*', '/', '!']
    for index in range(len(lst)):
        w = lst[index]
        if w.isalpha():
            word.append(w)
        elif w.isdigit():
            word.append(w)
        elif w == '_':
            word.append(w)
        else:
            if word:    # word 不为空
                word_list.append(''.join(word).strip())
                word = []
            if blank.match(w) is None:  # 匹配 w是否是空白字符
                if w in sign:
                    if lst[index-1] in sign:
                        op = lst[index-1] + w  # 如果sign中的任意两个字符相邻  则可能是组合操作符
                        word_list.pop()   # 删除最后一个元素
                    else:
                        op = w
                else:
                    op = w
                word_list.append(op)

    return word_list


def writefile(content):
    with open('log.txt', 'a') as f:
        f.write(content+'\n')


def main_work():
    lst = get_list()
    print lst
    for x in lst:
        if x in keywords:
            print u'关键字:', x
            writefile('关键字->  '+x)
        elif x in operator:
            print u'运算符:', x
            writefile('运算符->  '+x)
        elif x in division:
            print u'分界符:', x
            writefile('分界符->  '+x)
        elif x.isdigit():
            print u'常数:', x
            writefile('常数->  '+x)
        else:
            print u'标识符:', x
            writefile('标识符->  '+x)

if __name__ == '__main__':
    with open('log.txt', 'w'):
        print u'清空文件内容...'
        writefile('文件生成时间:'+time.strftime('%Y-%m-%d %H:%M:%S'))
    main_work()