# Author: bibberzz
# Created: 2026/5/29 16:58
# Project: day5
# File: all_is_citation.py
# Description: 一切皆引用

a = 10
print(id(a))    # get address
b = a
print(id(b))    # a, b same address, because of citation.
