# Author: bibberzz
# Created: 2026/5/27 20:08
# Project: day03
# File: accumulate.py
# Description: 实现从1到100之间的奇数求和

n = 0

for i in range(1, 101):
    if i % 2 != 0:
        n += i

print(f"1到100之间的奇数求和结果为：{n}")