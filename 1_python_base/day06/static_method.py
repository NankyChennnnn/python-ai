# Author: bibberzz
# Created: 2026/5/30 20:28
# Project: day6
# File: static_method.py
# Description: 静态方法，没有self


class MathHelper:
    # 静态方法：纯功能逻辑（判断是否为偶数）
    @staticmethod
    def is_even(num):
        return num % 2 == 0

    # 静态方法：纯功能逻辑（计算平均值）
    @staticmethod
    def average(a, b):
        return (a + b) / 2


# 调用静态方法（推荐用类名）
print(MathHelper.is_even(4))  # 输出：True
print(MathHelper.average(3, 5))  # 输出：4.0
