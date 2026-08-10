# Author: bibberzz
# Created: 2026/5/30 10:54
# Project: day5
# File: task1.py
# Description: 在函数内改变函数外某个列表中第一个元素的值（和上课代码原理保持一致即可）

def change_elem(origin_list):
    origin_list[0] = 4


if __name__ == '__main__':
    list1 = [1, 2, 3]
    print(f'origin list: {list1}')
    change_elem(list1)
    print(f'changed list: {list1}')
