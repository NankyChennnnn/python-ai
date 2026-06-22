# Author: bibberzz
# Created: 2026/6/2 14:18
# Project: day8
# File: copy_test.py
# Description:


a = [1, 2]
b = a
print(a, b)

b[0] = 3
print(a, b)

c = a.copy()
print(c)
c[0] = 4
print(a, c)

print(id(a), id(b), id(c))

d = [[1, 2], [3, 4]]
e = d.copy()
print(d, e)

e[0][1] = 5
print(d, e)

e[0] = [6, 7]
print(d, e)