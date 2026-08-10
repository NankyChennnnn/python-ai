# Author: bibberzz
# Created: 2026/5/30 17:07
# Project: day6
# File: rewrite.py
# Description:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, school):
        # 调用父类的__init__方法, *** super() ***
        super().__init__(name, age)  # 新增子类属性

        # 避免重写函数时造成的重复代码
        # self.name = name
        # self.age = age

        self.school = school

    def get_info(self):
        # 调用父类的属性，添加子类信息
        return f"{self.name}, {self.age}岁, 在{self.school}上学"


student = Student("张三", 15, "阳光中学")
print(student.get_info())  # 输出：张三, 15岁, 在阳光中学上学

