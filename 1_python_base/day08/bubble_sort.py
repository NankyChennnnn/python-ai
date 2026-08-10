# Author: bibberzz
# Created: 2026/6/3 09:36
# Project: day8
# File: bubble_sort.py
# Description:

import random


class BubbleSort:
    def __init__(self, count):
        """
        冒泡排序列表初始化
        :param count:
        """
        self.arr = []
        for i in range(count):
            self.arr.append(random.randint(0, 99))  # [0, 99]
        self.count = count

    # 时间复杂度：O(n**2)
    # 加入哨兵可提升至 O(n)
    def sort(self):
        arr = self.arr
        for i in range(self.count - 1, 0, -1):
            for j in range(i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == '__main__':
    qs = BubbleSort(10)
    print(qs.arr)
    qs.sort()
    print(qs.arr)
