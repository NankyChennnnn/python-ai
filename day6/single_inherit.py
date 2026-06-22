# Author: bibberzz
# Created: 2026/5/30 16:47
# Project: day6
# File: single_inherit.py
# Description:

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name}在吃东西")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        print(f"{self.name}没在吃东西")

    def bark(self):
        print(f"{self.name}在汪汪叫")


wangcai = Dog("wangcai")    # 如果自己有__init__会直接覆盖父类的，其他函数一样
wangcai.eat()
wangcai.bark()
