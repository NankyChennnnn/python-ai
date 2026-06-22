# Author: bibberzz
# Created: 2026/5/27 20:13
# Project: day03
# File: timesTable.py
# Description: 打印九九乘法表

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{i} x {j} = {i * j}", end="\t")
    print()
