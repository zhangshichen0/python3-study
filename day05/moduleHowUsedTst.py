#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 命令行运行时，必须加入前两行
# 常用的模块 sys os fileinput webbroser

# 运行
# python3 moduleHowUsedTst.py moduleHowUsedTst.py

# fileinput的使用

import fileinput
import webbrowser

# inplace=True 会直接修改文件  False会输出到控制台,读取的命令行输入的文件
for line in fileinput.input(inplace=False):
    line = line.rstrip()
    num = fileinput.lineno()
    print("%-50s # %2i" % (line, num))

# 打开浏览器
webbrowser.open("http://www.baidu.com")
