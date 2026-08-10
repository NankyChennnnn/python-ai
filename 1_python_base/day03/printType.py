# Author: bibberzz
# Created: 2026/5/27 16:48
# Project: day03
# File: printType.py
# Description: annotation and variable

# 输出
# print('hello world')


def myfunc():
    # this is a function

    """
    this is a function
    :return:
    """
    pass


myfunc()

name = 'zs'         # 定义了第一个变量，变量名是'name', 它的值是'zs'
age = 20            # 定义了第二个变量
height = 180.5      # 定义了第三个变量

print(type(name))
print(type(age))
print(type(height))
