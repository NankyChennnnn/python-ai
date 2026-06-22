# Author: bibberzz
# Created: 2026/6/2 10:59
# Project: day7
# File: task2.py
# Description: 传递参数file1，通过sys.argv[1]打开文件，读取里边的内容并打印
# 如果传递的参数是file2，程序同样可以打印file2的文件内容

import sys


def open_file():
    f = open(sys.argv[1], 'r', encoding='utf8')
    print(f.read())


if __name__ == '__main__':
    open_file()
