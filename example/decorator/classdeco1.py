# -*- coding: utf-8 -*-
# @Time     : 2019/5/18 16:21
# @Author   ：Wang Guosong
# @File     : classdeco1.py
# @Software : PyCharm

instances = {}

def singleton(aClass):
    def onCall(*args, **kwargs):
        if aClass not in instances:
            instances[aClass] = aClass(*args, **kwargs)
        return instances[aClass]
    return onCall

def singleton(aClass): # On @ decoration
    instance = None
    def onCall(*args, **kwargs): # On instance creation
        nonlocal instance # 3.X and later nonlocal
        if instance == None:
            instance = aClass(*args, **kwargs) # One scope per class
        return instance
    return onCall


@singleton
class Person:
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate
    def pay(self):
        return self.hours * self.rate

@singleton
class Spam:
    def __init__(self, val):
        self.attr = val

if __name__ == '__main__':
    bob = Person('Bob', 40, 10)
    print(bob.name, bob.pay())

    sue = Person('Sue', 50, 20)
    print(sue.name, sue.pay())

    X = Spam(val=42)
    Y = Spam(99)
    print(X.attr, Y.attr)