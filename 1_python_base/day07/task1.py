# Author: bibberzz
# Created: 2026/6/2 10:29
# Project: day7
# File: task1.py
# Description: 通过try进行异常捕捉，确保输入的内容一定是一个整型数，
# 然后判断该整型数是否是对称数，12321就是对称数，
# 123321也是对称数，否则就打印不是，非整型抛异常，不是对称数抛异常

def is_symmetric(num):
    s = str(num)
    return s == s[::-1]


def get_int():
    num_str = input('Please input an int number: ')
    try:
        num = int(num_str)
        if is_symmetric(num):
            print(f'{num} is a symmetric number.')
        else:
            raise Exception(f'[ERROR] {num} is not a symmetric number.')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    get_int()
