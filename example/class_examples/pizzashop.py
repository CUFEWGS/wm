# -*- coding: utf-8 -*-
# @Time     : 2019/5/28 10:31
# Author    ：Wang Guosong
# @File     : pizzashop.py
# @Software : PyCharm

# from __future__ import print_function
from example.class_examples.employees import PizzaRobot, Server

class Customer:
    def __init__(self, name):
        self.name = name
    def order(self, server):
        print(self.name, "orders from", server)
    def pay(self, server):
        print(self.name, "pays for item to", server)


class Oven:
    def bake(self):
        print("oven bakes")

class PizzaShop:
    def __init__(self):
        self.server = Server('Pat')
        self.chef = PizzaRobot('Bob')
        self.oven = Oven()

    def order(self, name):
        customer = Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)

if __name__ == '__main__':
    scene = PizzaShop()
    scene.order('Homer')
    print('...')
    scene.order('Shaggy')


# mark a sentence here for class:
#    As a thumb, classes can represent just about any objects and relationships you can ecpress in a sentence;
#    just replace nouns with class, and verbs with methods, and you'll have a fist cut at a design
