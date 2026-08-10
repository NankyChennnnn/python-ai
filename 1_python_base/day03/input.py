# Author: bibberzz
# Created: 2026/5/27 17:18
# Project: day03
# File: input.py
# Description: input test

age = input('请输入您的年龄：')

print(type(age))

new_age = int(age)  # cant change '8.5' to float, throw error
print(f"{type(new_age)}, {new_age}")
