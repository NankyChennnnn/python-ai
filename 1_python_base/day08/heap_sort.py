# Author: bibberzz
# Created: 2026/6/3 10:17
# Project: day8
# File: heap_sort.py
# Description:

import random


class HeapSort:
    def __init__(self, count):
        """
        堆排初始化，大根堆
        :param count:
        """
        self.arr = []
        for i in range(count):
            self.arr.append(random.randint(0, 99))  # [0, 99]
        self.count = count

    def adjust(self, adjust_pos, arr_len):
        """
        调整某课子树为大根堆
        :param adjust_pos: 调整子树的父亲节点下标
        :param arr_len: 列表长度
        :return:
        """
        arr = self.arr
        dad = adjust_pos
        son = 2 * dad + 1
        while son < arr_len:
            if son + 1 < arr_len and arr[son] < arr[son + 1]:
                son += 1

            if arr[son] > arr[dad]:
                arr[son], arr[dad] = arr[dad], arr[son]

                dad = son
                son = 2 * dad + 1
            else:
                break

    # 时间复杂度 O(nlog2n)
    def sort(self):
        arr = self.arr

        # 创建大根堆
        for dad in range(self.count // 2 - 1, -1, -1):
            self.adjust(dad, self.count)

        # 排序，固定元素
        for arr_len in range(self.count - 1, 0, -1):
            arr[0], arr[arr_len] = arr[arr_len], arr[0]
            self.adjust(0, arr_len)


if __name__ == '__main__':
    hs = HeapSort(10)
    print(hs.arr)
    hs.sort()
    print(hs.arr)