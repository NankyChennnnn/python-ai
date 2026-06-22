# Author: bibberzz
# Created: 2026/5/28 16:52
# Project: day4
# File: operatorTest.py
# Description:

def use_bit():
    """
    练习位运算
    :return:
    """

    # 0000 0101 : 5
    # 0000 0111 : 7
    print(5 & 7)    # 0000 0101 : 5
    print(5 | 7)    # 0000 0111 : 7
    print(~5)       # 按位取反 1111 1010 -> 负数补码 1000 0101 -> 补码加1 1000 0110 : -6
    print(5 ^ 7)    # 0000 0010 : 2
    print(5 << 1)   # 0000 1010 : 10
    print(8 >> 1)   # 0000 1000 -> 0000 0100 : 4
    print(7 >> 1)   # 0000 0011 : 3
    print(-8 >> 1)  # 原 1000 1000 -> 补 1111 1000 -> 右移 1111 1100 -> 反补 1000 0100 : -4
    print(-7 >> 1)  # 原 1000 0111 -> 补 1111 1001 -> 右移 1111 1100 -> 反补 1000 0100 : -4


def bit_homework():
    """
    异或运算练习（异或满足交换律和结合律；相同数字异或结果为 0，任何数字和 0 异或还是自己）
    注意，这个方法成立的前提是：只有一个数字出现一次；其他数字都恰好出现两次。
    如果有两个数字只出现一次，或者其他数字出现三次，这个简单异或法就不能直接得到唯一答案。
    :return:
    """
    my_list = [4, 5, 3, 5, 4, 2, 2]
    result = 0
    for i in my_list:
        print(f'{result} ^ {i} = {result:08b} ^ {i:08b}', end=" ")
        result ^= i
        print(f'= {result:08b} = {result}')


def ternary():
    """
    三目运算符练习
    :return:
    """
    a = 10
    b = 5
    max_num = a if a > 0 else b
    print(max_num)


# bit_homework()
ternary()