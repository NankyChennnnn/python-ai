# Author: bibberzz
# Created: 2026/5/30 10:57
# Project: day5
# File: task2.py
# Description: 练习位置参数，keyword参数，同时练习当你传递位置参数，keyword不正确的时候，
# 出现报错信息，理解报错原因。正确代码可以提交，错误代码也可以提交，在错误代码后面贴上报错文
# 字即可。（和上课代码原理保持一致即可）

def test1(a, b):
    return a + b


def test2(a, b=2):
    return a + b


def test3(a=1, b=2):
    return a + b


# # SyntaxError: parameter without a default follows parameter with a default
# def test4(a = 1, b):
#     return a + b

if __name__ == '__main__':
    r1 = test1(1, 2)
    print(f'test1 result: {r1}')
    # test1(1)    # TypeError: test1() missing 1 required positional argument: 'b'

    r2 = test2(1)
    print(f'test2 result: {r1}')
    r3_1 = test3()
    print(f'test3() result: {r3_1}')
    r3_2 = test3(2)
    print(f'test3(2) result: {r3_2}')
