# Author: bibberzz
# Created: 2026/6/1 17:21
# Project: day7
# File: use_file.py
# Description:

def file_open():
    file1 = open('file.txt', 'r', encoding='utf8')
    txt = file1.read()
    print(txt)
    file1.close()


if __name__ == '__main__':
    file_open()
