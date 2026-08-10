# Author: bibberzz
# Created: 2026/5/29 14:16
# Project: day4
# File: task1.py
# Description:

num_str = "0123456789"

str_2_5 = num_str[2:6]
print(f'截取从 2 ~ 5 位置（是指下标） 的字符串: {str_2_5}')

str_2_end = num_str[2:]
print(f'截取从 2 ~ 末尾的字符串: {str_2_end}')

str_begin_5 = num_str[:6]
print(f'截取从 开始~ 5 位置 的字符串: {str_begin_5}')

str_begin_end = num_str[::]
print(f'截取完整的字符串: {str_begin_end}')

str_step2 = num_str[::2]
print(f'从开始位置，每隔一个字符截取字符串: {str_step2}')

str_1_step2 = num_str[1::2]
print(f'从索引 1 开始，每隔一个取一个: {str_1_step2}')

print(f'\n这里存在歧义，所以保留了两版。')
print(f'我觉得2~末尾-1即'
      f'num_str[2]={num_str[2]} ~ num_str[-1]={num_str[-1]}，'
      f'所以保留了最后一个字符：')
str_2__1 = num_str[2:]
print(f'截取从 2 ~  末尾-1 的字符串: {str_2__1}')
print(f'如果不保留则是num_str[2:-1]：')
str_2__1 = num_str[2:-1]
print(f'截取从 2 ~  末尾-1 的字符串: {str_2__1}\n')
print('-'*100)
print(f'[INFO] 更正信息：按照 Python 切片规则，“末尾-1”通常表示最后一个元素之前的位置，因此标准答案一般为 num_str[2:-1]')
print('-'*100)
print('\n')


str__1__2 = num_str[-2:]
print(f'截取字符串末尾两个字符: {str__1__2}')

list_num_str = list(num_str)
list_num_str.reverse()
reversed_num_str1 = ''.join(list_num_str)
print(f'字符串的逆序1: {reversed_num_str1}')

reversed_num_str2 = num_str[::-1]
print(f'字符串的逆序2: {reversed_num_str2}')

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
enum_seasons = enumerate(seasons)
_dict = {}
for key, value in enum_seasons:
    _dict[key] = value

print(f'Change seasons list to a dict: {_dict}')
