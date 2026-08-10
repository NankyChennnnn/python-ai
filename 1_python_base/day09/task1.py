# Author: bibberzz
# Created: 2026/6/3 16:12
# Project: day9
# File: task1.py
# Description: 练习sorted的各种使用

def sort_list():
    """
    sort 前后列表不共享空间
    :return:
    """
    nums = [3, 1, 4, 2]
    sorted_nums = sorted(nums)
    print("原列表：", nums)
    print("排序后：", sorted_nums)


def sort_dict_default():
    """
    sort dict 的时候，默认用key进行排序，根据ASCII码逐个字符比较
    :return:
    """
    dict1 = {
        'name': 'zs',
        'age': 20,
        'gender': 'male',
        'height': 180}
    print(sorted(dict1))


def sort_list_len():
    words = ["apple", "banana", "cat", "dog"]
    # key是比较规则，传进的是一个函数，函数的入参，是可迭代对象的某一个元素
    print(f'key=len: {sorted(words, key=len)}')
    print(f'key=str.lower: {sorted(words, key=str.lower)}')


def compare(x):
    return x['score']


def sort_list_dict():
    """
    排序列表内元素是字典
    :return:
    """
    students = [
        {"name": "Alice", "age": 18, "score": 98},
        {"name": "Bob", "age": 16, "score": 89},
        {"name": "Charlie", "age": 20, "score": 95}
    ]

    print(sorted(students, key=lambda x: x['age']))
    print(sorted(students, key=lambda x: (x['age'], -x['score'])))
    print(sorted(students, key=compare))
    print(sorted(students, key=compare, reverse=True))


def sort_two_col():
    """
    第一列升序，第二列降序
    :return:
    """
    list_tup = [(3, 5), (1, 2), (2, 4), (3, 1), (1, 3)]

    # default
    print(sorted(list_tup))

    # x --> list_tup
    # x[0] --> 第一列
    # x[1] --> 第二列
    # '-' --> 降序
    print(sorted(list_tup, key=lambda x: (x[0], -x[1])))


def sort_dict_lambda():
    students = {
        'zhangsan': 98.5,
        'lisi': 67,
        'wangwu': 88
    }

    # items() --> get "key: value", 2d tuple
    # x[1] --> get items()'s second element to sort
    # reverse sort
    print(sorted(students.items(), key=lambda x: x[1], reverse=True))


if __name__ == '__main__':
    print('sort_list() result: ')
    sort_list()
    print('-' * 50)

    print('sort_dict_default() result: ')
    sort_dict_default()
    print('-' * 50)

    print('sort_list_len() result: ')
    sort_list_len()
    print('-' * 50)

    print('sort_list_dict() result: ')
    sort_list_dict()
    print('-' * 50)

    print('sort_two_col() result: ')
    sort_two_col()
    print('-' * 50)

    print('sort_dict_lambda() result: ')
    sort_dict_lambda()
    print('-' * 50)
