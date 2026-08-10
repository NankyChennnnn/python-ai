# Author: bibberzz
# Created: 2026/5/28 16:27
# Project: day03
# File: and_or.py
# Description:


# A and B:
#   1. if A is false, return A; if A is true, return B;
#   2. both True return True, any False return False
# A or B:
#   1. if A is true, return A; if A is false, return B;
#   2. both False return False, any True return True

print(0 and 10)        # 0
print(5 and 10)        # 10
print('' and 'hello')  # ''
print('hi' and 'ok')   # ok

print(0 or 10)          # 10
print(5 or 10)          # 5
print('' or 'default')  # default
print('hi' or 'ok')     # hi
