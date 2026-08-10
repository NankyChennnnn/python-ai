# Author: bibberzz
# Created: 2026/6/3 11:42
# Project: day8
# File: task2.py
# Description: 练习上课的search，findall,sub，split等案例

import re


def search():
    """
    只匹配第一个
    :return:
    """
    text = "我的手机号：13812345678，备用号：13987654321"
    pattern = r"1[34578]\d{9}"

    result = re.search(pattern, text)
    if result:
        print("第一个手机号：", result.group())  # 输出：第一个手机号：13812345678
        print("位置：", result.span())  # 输出：位置：(6, 17)（起始/结束索引）
    else:
        print('未匹配')


def findall():
    """
    全匹配，list 形式输出
    :return:
    """
    text = "我的手机号：13812345678，备用号：13987654321"
    pattern = r"1[34578]\d{9}"

    result = re.findall(pattern, text)
    if result:
        print(result)
    else:
        print('未匹配')


def sub():
    """
    内容替换
    :return:
    """
    text1 = "这个内容是垃圾，不要传播黄色信息"
    pattern = r"垃圾|黄色"
    new_text = re.sub(pattern, "*", text1)  # 替换匹配内容为*
    print(new_text)

    text2 = '视频播放量 1000 次'
    new_text = re.sub(r'\d+',
                      lambda ret: str(int(ret.group()) * 2),
                      text2)
    print(new_text)


def split():
    text = "apple banana,orange;grape"
    pattern = r"[ ,;]"  # 匹配空格、逗号、分号中的任意一个

    result = re.split(pattern, text)
    print("分割结果：", result)


if __name__ == '__main__':
    print('search test')
    search()

    print('\nfindall test')
    findall()

    print('\nsub test')
    sub()

    print('\nsplit test')
    split()
