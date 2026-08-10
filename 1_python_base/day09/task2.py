# Author: bibberzz
# Created: 2026/6/3 16:45
# Project: day9
# File: task2.py
# Description: 通过自己写的hash函数，实现美女与野兽小说的单词词频为前10的统计
# 输入结果如下（供参考，因为分词方法的差异可以造成不同）：
# ['to', 245] ['and', 240] ['the', 239] ['she', 151]
# ['was', 113] ['her', 104] ['he', 103] ['of', 99]
# ['that', 96] ['a', 93]

import re


class MyHashTable:
    def __init__(self, capacity=1000):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]

    # 核心 hash 算法函数
    def hash_func(self, word):
        hash_value = 0

        for ch in word:
            hash_value = hash_value * 31 + ord(ch)

        return hash_value % self.capacity

    def add(self, word):
        index = self.hash_func(word)
        # 如果 hash_value 相同，会被装在同一个 bucket 中
        # 所以 table 是一个 list，其中包含了 capacity 个 list 作为 bucket
        # bucket 中又包含了多个 tuple
        bucket = self.table[index]

        # 遍历 bucket 拿到所有 tuple
        for i, item in enumerate(bucket):
            key, count = item  # 拿到元组中的单词和词频
            if key == word:  # 对比单词是否匹配
                bucket[i] = (key, count + 1)  # 匹配则词频 +1
                return  # 已找到不必继续循环

        # 如果遍历了还没找到，插入新元组
        bucket.append((word, 1))

    def top10(self):
        origin = []
        for bucket in self.table:
            for key, count in bucket:
                origin.append([key, count])

        result = sorted(origin, key=lambda x: x[1], reverse=True)

        for item in result[:10]:
            print(item, end='')


if __name__ == '__main__':
    hash_table = MyHashTable()
    with open('Beauty and The Beast.txt', 'r', encoding='utf8') as file:
        for line in file:
            words = re.findall(r"[a-zA-Z]+", line.lower())

            for word in words:
                hash_table.add(word)

    hash_table.top10()
