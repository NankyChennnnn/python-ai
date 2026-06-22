# Author: bibberzz
# Created: 2026/5/30 16:04
# Project: day6
# File: private_method.py
# Description:

class Girl:
    def __init__(self, age):
        self.__age = age

    def __secret(self):
        """
        "__" also means private in function name setting
        private method cannot use out of class
        :return:
        """
        print(self.__age)

    def boyfriend(self):
        self.__secret()


xiaohong = Girl(20)
# print(xiaohong.__age)  # AttributeError: 'Girl' object has no attribute '__age'
# xiaohong.__secret()  # AttributeError: 'Girl' object has no attribute '__secret'
xiaohong.boyfriend()  # ok
