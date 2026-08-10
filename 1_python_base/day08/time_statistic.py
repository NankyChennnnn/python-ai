# Author: bibberzz
# Created: 2026/6/3 10:53
# Project: day8
# File: time_statistic.py
# Description:

import time
from bubble_sort import BubbleSort
from quick_sort import QuickSort
from heap_sort import HeapSort


class TimeStatistic:
    def use_time(self, sort_func, *args):
        start = time.time()
        sort_func(*args)
        end = time.time()
        print(f'use time: {end - start}')


if __name__ == '__main__':
    ts = TimeStatistic()

    bs = BubbleSort(1000)
    print("Bubble sort", end=' ')
    ts.use_time(bs.sort)    # 传递函数是使用 对象.函数名 的方式，不用加小括号
    print()

    qs = QuickSort(1000)
    print("Quick sort", end=' ')
    ts.use_time(qs.sort, 0, qs.count - 1)
    print()

    hs = HeapSort(1000)
    print("Heap sort", end=' ')
    ts.use_time(hs.sort)
    print()
