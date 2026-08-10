# Author: bibberzz
# Created: 2026/5/29 16:38
# Project: day5
# File: variable_length_args.py
# Description:

def sub_total(*args):
    """
    *args 会吃掉所有位置参数
    :param args:
    :return:
    """
    print(f'sum: {sum(args)}')


def print_user_info(**kwargs):
    print(kwargs)


def demo1(*args, **kwargs):
    print(f'demo1 {args}')
    print(f'demo1 {kwargs}')


def demo(*args, **kwargs):
    print(f'demo {args}')
    print(f'demo {kwargs}')
    demo1(*args, **kwargs)


sub_total(1, 2, 3, 4, 5)
print_user_info(name='xiaogang', age=20, gender='male')
demo(1, 2, 3, 4, name='xiaogang', age=20)

# *****
# 拆包方式交换
a, b = 1, 2
a, b = b, a

# b, a --> 打包成元组 (b, a) --> a, b = (b, a) 拆包赋值
