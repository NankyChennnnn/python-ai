# Author: bibberzz
# Created: 2026/6/3 15:05
# Project: day9
# File: hash_search.py
# Description:

MAXKEY = 1000


def elf_hash(hash_str):
    h = 0
    g = 0
    for i in hash_str:
        h = (h << 4) + ord(i)
        g = h & 0xf0000000
        if g:
            h ^= g >> 24
            h &= ~g

    return h % MAXKEY


def use_hash():
    str_list = ["xiongda", "lele", "hanmeimei", "wangdao", "fenghua"]
    hash_table = [None] * MAXKEY
    for name in str_list:
        hash_table[elf_hash(name)] = name


if __name__ == '__main__':
    print("cursor test")
