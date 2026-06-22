# Author: bibberzz
# Created: 2026/6/1 14:29
# Project: day7
# File: exception_transmission.py
# Description:

def demo1():
    content = input("请输入一个整数:")
    num = int(content)
    return num


def demo2():
    demo1()


if __name__ == '__main__':
    # 直接调用
    demo2()

    # 也可以在主程序主动捕获异常
    # try:
    #     demo2()
    # except Exception as e:
    #     # 处理异常