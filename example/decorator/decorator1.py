# -*- coding: utf-8 -*-
# @Time     : 2019/5/18 16:21
# @Author   ：Wang Guosong
# @File     : decorator1.py
# @Software : PyCharm

class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func
    def __call__(self, *args):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        self.func(*args)


@tracer
def spam(a, b, c):
    print(a + b + c)

class Person:
    def __init__(self, name, pay):
        self.name =  name
        self.pay = pay

    @tracer
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    @tracer
    def lastName(self):
        return self.name.split()[-1]

if __name__ == '__main__':
    spam(1, 2, 3)
    spam('a', 'b', 'c')
    spam.calls
    spam
    bob = Person('Bob Smith', 50000)
    bob.giveRaise(0.25)
    print(bob.lastName())
