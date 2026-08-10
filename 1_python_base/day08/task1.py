# Author: bibberzz
# Created: 2026/6/3 11:21
# Project: day8
# File: task1.py
# Description: 练习上课匹配单个字符，多个字符，匹配分组的正则表达式案例

import re


def single():
    """
    单个字符
    :return:
    """
    pattern = r"[a-z]\d[a-z]"
    texts = ["a1b", "B2C", "x3y", "1ab"]
    for text in texts:
        if re.match(pattern, text):
            print(f'{text} matched.')
        else:
            print(f'{text} match failed.')


def multi():
    """
    多个字符
    :return:
    """
    texts = ["20", "3", "abc", "123abc",
             "abc", "abcd12", "ab", "abcdef", "AbC12"]

    pattern1 = r"\d+"
    for text in texts:
        ret = re.match(pattern1, text)
        print(f'{text}: '
              f'{f'matched {ret.group()}' if ret else 'match failed'}')

    print()

    pattern2 = r"[a-zA-Z]{3,6}"
    for text in texts:
        print(f'{text}: '
              f'{re.match(pattern2, text) is not None}')


def group():
    """
    匹配分组
    :return:
    """
    # '+' : 1次或多次
    # () 为一组，[1, ...]
    pattern = r"([a-zA-Z0-9_\.]+)@([a-zA-Z0-9]+\.[a-zA-Z]{2,4}$)"
    emails = ["user@163.com", "user@.com", "abc@123", "user@163.com.abc",
              "user_1@163.com"]
    for email in emails:
        ret = re.match(pattern, email)
        if ret:
            print(f'{email} 是合法邮箱，', end='')
            print(f'用户名 {ret.group(1)}，', end='')
            print(f'域名 {ret.group(2)}')
        else:
            print(f'{email} 不是合法邮箱')


if __name__ == '__main__':
    single()
    print('-' * 50)

    multi()
    print('-' * 50)

    group()
    print('-' * 50)
