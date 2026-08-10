# Author: bibberzz
# Created: 2026/5/30 20:22
# Project: day6
# File: class_attribute_method.py
# Description:


class Student:
    school = "北京大学" # class attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} {self.age}岁，在{self.school}上学'

    @classmethod
    def show_school(cls):
        print(f'{cls.school}')  # 访问类属性


stu1 = Student('xiaogang', 20)
print(stu1)
Student.school = "清华大学"
print(stu1)

Student.show_school()