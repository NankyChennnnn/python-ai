# Author: bibberzz
# Created: 2026/6/3 14:10
# Project: day8
# File: task4.py
# Description: 完成快排、堆排

import random


class Sort:
    def __init__(self, count):
        self.arr = []
        self.count = count

        for i in range(count):
            self.arr.append(random.randint(0, 99))

    def get_pivot(self, left, right):
        arr = self.arr
        k = left

        for i in range(left, right):
            if arr[i] < arr[right]:
                arr[i], arr[k] = arr[k], arr[i]
                k += 1

        arr[k], arr[right] = arr[right], arr[k]
        return k

    def quick_sort(self, left, right):
        if left < right:
            pivot = self.get_pivot(left, right)
            self.quick_sort(left, pivot - 1)
            self.quick_sort(pivot + 1, right)

    def adjust_max_heap(self, pos, arr_len):
        arr = self.arr
        dad = pos
        son = 2 * dad + 1
        while son < arr_len:
            if son + 1 < arr_len and arr[son] < arr[son + 1]:
                son += 1

            if arr[dad] < arr[son]:
                arr[dad], arr[son] = arr[son], arr[dad]
                dad = son
                son = 2 * dad + 1
            else:
                break

    def heap_sort(self):
        arr = self.arr

        # 创建大根堆，当前状态下最大值上浮至根节点
        for dad in range(self.count // 2 - 1, -1, -1):
            self.adjust_max_heap(dad, self.count)

        for arr_len in range(self.count - 1, 0, -1):
            # 固定最大值到末尾
            arr[0], arr[arr_len] = arr[arr_len], arr[0]

            # 缩小范围再次上浮
            self.adjust_max_heap(0, arr_len)


if __name__ == '__main__':
    sort = Sort(10)
    print(sort.arr)
    sort.quick_sort(0, sort.count - 1)
    print(sort.arr)

    print('-' * 40)

    sort1 = Sort(10)
    print(sort1.arr)
    sort1.heap_sort()
    print(sort1.arr)
