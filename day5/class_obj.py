# Author: bibberzz
# Created: 2026/5/30 10:13
# Project: day5
# File: class_obj.py
# Description:

class Car:
    def run(self):
        print("Car starts running.")


car1 = Car()
car1.run()

# 不规范初始化
car1.brand = 'xiaomi'
car1.color = 'green'

print(car1.brand)


class Person:
    def __init__(self, name, age):
        """
        规范初始化
        只可以在init中给对象添加属性，业界规范
        :param name:
        :param age:
        """
        self.name = name
        self.age = age

    def play(self):
        self.study()  # 可行，相当于声明和定义都放在一起了
        # 整个类中出现过，就是声明过了，能直接找到
        print(f'{self.name} is playing games.')

    def study(self):
        print('Study first.')

    def __str__(self):
        """
        必须返回字符串类型，修改print(obj)时的输出内容，原始内容为对象地址
        :return:
        """
        return f'name: {self.name}, age: {self.age}'

    def __del__(self):
        print(f'{self.name} is delete.')


if __name__ == '__main__':
    xiaoming = Person('xiaoming', 20)
    xiaoming.play()
    print(xiaoming)
    del xiaoming
