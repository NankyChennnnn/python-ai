# Author: bibberzz
# Created: 2026/6/3 09:32
# Project: day8
# File: quick_sort.py
# Description:

import random


class QuickSort:
    def __init__(self, count):
        """
        快排列表初始化
        :param count: 排序的元素数目
        """
        self.arr = []
        for i in range(count):
            self.arr.append(random.randint(0, 99))  # [0, 99]
        self.count = count

    def partition(self, left, right):
        """
        拿最右边作为分割点，把比分割点小的放到分割点左边，大的放到右边
        :param left:
        :param right:
        :return: 分割点下标
        """
        arr = self.arr
        k = left

        # 为了避免最坏时间复杂度
        save_idx = random.randint(left, right - 1)
        arr[right], arr[save_idx] = arr[save_idx], arr[right]

        for i in range(left, right):  # [left, right - 1]，固定 arr[right]
            if arr[i] < arr[right]:  # 如果 arr[i] 比 arr[right] 小
                arr[i], arr[k] = arr[k], arr[i]  # 就让 i,k 位置元素交换
                k += 1  # k 右移

        arr[k], arr[right] = arr[right], arr[k]  # 最后 k 为要找的 pivot
        return k

    def sort(self, left, right):
        if left < right:
            pivot = self.partition(left, right)
            self.sort(left, pivot - 1)
            self.sort(pivot + 1, right)


if __name__ == '__main__':
    qs = QuickSort(10)
    print(qs.arr)
    qs.sort(0, qs.count - 1)
    print(qs.arr)
