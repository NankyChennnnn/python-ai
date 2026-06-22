# Author: bibberzz
# Created: 2026/5/30 20:58
# Project: day6
# File: task3.py
# Description:

class Student:
    school = "Tsinghua University"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def show_school(cls):
        print(f'{cls.school}')

    @staticmethod
    def get_notice():
        print('This is a notice')


stu1 = Student('xiaoming', 20)
stu2 = Student('xiaohong', 22)
print(stu1.school)
print(stu2.school)

print("-"*50)
stu1.school = "Peking University"
print(stu1.school)
print(stu2.school)

print("-"*50)
Student.school = "HIT"
print(stu1.school)
print(stu2.school)

print("-"*50)
stu1.get_notice()
Student.get_notice()
