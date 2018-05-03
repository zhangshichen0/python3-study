#!/usr/bin/python3
# -*- coding: utf-8 -*-

# cat test.txt | python3 wordCountScript.py

# 计算文件的单词数量
import sys
text = sys.stdin.read()
words = text.split()
wordcount = len(words)
print('Word count:', wordcount)
