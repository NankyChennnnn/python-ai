# Author: bibberzz
# Created: 2026/5/30 20:35
# Project: day6
# File: singleton.py
# Description:

class Singleton(object):
    instance = None  # class attribute

    def __new__(cls, *args, **kwargs):
        """
        __new__ == malloc(C) == new(C++)
        :param args:
        :param kwargs:
        """

        # 如果实例不存在，创建
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, name):
        self.music_name = name


music_player = Singleton("七里香")
print(music_player.music_name)

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)   # True
print(a is b)   # False
print(id(a), id(b))