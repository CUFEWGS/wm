# -*- coding: utf-8 -*-
# @Time     : 2019/5/28 14:42
# Author    ：Wang Guosong
# @File     : testmixin0.py
# @Software : PyCharm

from example.class_examples.listinstance import ListInstance

class Super:
    def __init__(self):
        self.data1 = 'spam'
    def ham(self):
        pass

class Sub(Super, ListInstance):
    def __init__(self):
        Super.__init__(self)
        self.data2 = 'eggs'
        self.data3 = 42

    def spam(self):
        pass

if __name__ == '__main__':
    X = Sub()
    print(X)