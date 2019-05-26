# -*- coding: utf-8 -*-
# @Time     : 2019/5/26 15:51
# Author    ：Wang Guosong
# @File     : person.py
# @Software : PyCharm

from example.class_examples.classtools import AttrDisplay


class Person(AttrDisplay):
    """
    Create and process person records
    """
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    # def __repr__(self):
        # return '[Person: %s, %s]' % (self.name, self.pay)
    # def __str__(self):
    #     return 'Person: %s, %s' % (self.name, self.pay)


class Manager(Person):
    """
    A customised Person with special requirements
    """
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def giveRaise(self, percent, bonus=0.10):
        Person.giveRaise(self, percent + bonus)

class Department:
    def __init__(self, *args):
        self.members = list(args)

    def addMember(self, person):
        self.members.append(person)

    def giveRaise(self, percent):
        for person in self.members:
            person.giveRaise(percent)

    def showAll(self):
        for person in self.members:
            print(person)



if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    # print(bob.name, bob.pay)
    # print(sue.name, sue.pay)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(0.10)
    print(sue.pay)
    print(sue)
    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(0.1)
    print(tom.lastName())
    print(tom)

    # department = Department(bob, sue)
    # department.addMember(tom)
    # department.giveRaise(0.1)
    # department.showAll()


