# Author: bibberzz
# Created: 2026/5/30 11:04
# Project: day5
# File: task3.py
# Description: 多值参数练习，元组，字典的传参拆包练习（和上课代码原理保持一致即可）

def test1(*args):
    """

    :param args: get all position args --> tuple
    :return:
    """
    print(f'sum = {sum(args)}')


def test2(**kwargs):
    """

    :param kwargs: get all keywords args --> dict
    :return:
    """
    print(kwargs)


def test3(*args, **kwargs):
    print(f'Get args: {args}')
    print(f'Get kwargs: {kwargs}')


def test4(*args, **kwargs):
    print(f'Get test3 result from test4:')
    test3(*args, **kwargs)


if __name__ == '__main__':
    test1(1, 2, 3, 4)
    print("-"*100)
    test2(name='xiaoming', age=20, gender='male')
    print("-"*100)
    test3(1, 2, 3, 4, name='xiaoming', age=20, gender='male')
    print("-"*100)
    test4(5, 6, 7, 8, name='xiaohong', age=21, gender='female')
