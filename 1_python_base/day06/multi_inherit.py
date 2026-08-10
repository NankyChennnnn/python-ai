# Author: bibberzz
# Created: 2026/5/30 16:53
# Project: day6
# File: multi_inherit.py
# Description:

# 父类1
class Flyable:
    def fly(self):
        print("会飞")


# 父类2
class Swimmable:
    def swim(self):
        print("会游泳")


# 子类继承多个父类
class Duck(Flyable, Swimmable):
    pass


# 使用子类
duck = Duck()
duck.fly()  # 继承Flyable → 会飞
# 如果两个父类都有fly函数，会按继承顺序来调用第一个fly函数
print(Duck.__mro__)  # mro查找顺序 C3算法

duck.swim()  # 继承Swimmable → 会游泳


class A:  # 祖父类
    def say(self):
        print("A的say方法")


class B(A):  # 父类1，继承A
    def say(self):
        print("B的say方法")


class C(A):  # 父类2，继承A
    def say(self):
        print("C的say方法")


class D(B, C):  # 子类，继承B和C
    pass  # 未重写say方法


# 问题：D的对象调用say()，会执行B还是C的方法？
d = D()
d.say()  # 输出：B的say方法（为什么？）
# 先继承 B，虽然B继承了A，但是B中的say把A的覆盖了，调用的还是B的
