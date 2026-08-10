# Author: bibberzz
# Created: 2026/5/30 21:08
# Project: day6
# File: task4.py
# Description: Singleton

class Singleton:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, name):
        self.name = name


music_player1 = Singleton('彩虹')
print(music_player1.name)

music_player2 = Singleton('稻香')
print(music_player1.name)
print(music_player2.name)

print(music_player1 is music_player2)
