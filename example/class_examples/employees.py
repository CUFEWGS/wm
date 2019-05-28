# -*- coding: utf-8 -*-
# @Time     : 2019/5/28 10:11
# Author    ：Wang Guosong
# @File     : employees.py
# @Software : PyCharm

from __future__ import print_function


class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary
    def giveRaise(self, percent):
        self.salary = self.salary + (self.salary * percent)
    def work(self):
        print(self.name, "does stuff")
    def __repr__(self):
        return "<Employee: name=%s, salary=%s>" % (self.name, self.salary)


class Chef(Employee):
    def __init__(self, name):
        Employee.__init__(self, name,50000)
    def work(self):
        print(self.name, "makes food")

class Server:
    def __init__(self, name):
        Employee.__init__(self, name, 40000)

    def work(self):
        print(self.name, "interfaces with customer")

class PizzaRobot(Chef):
    def __init__(self, name):
        Chef.__init__(self, name)
    def work(self):
        print(self.name, "makes pizza")


if __name__ == '__main__':
    bob =  PizzaRobot('bob')
    print(bob)
    bob.work()
    bob.giveRaise(0.2)
    print(bob);print()

    for klass in Employee, Chef, Server, PizzaRobot:
        obj = klass(klass.__name__)
        obj.work()
