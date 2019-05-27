# -*- coding: utf-8 -*-
# @Time     : 2019/5/26 21:50
# Author    ：Wang Guosong
# @File     : test.py
# @Software : PyCharm

X = 11 # Global in module
def g1():
    print(X) # Reference global in module (11)

def g2():
    global X
    X = 22 # Change global in module

def h1():
    X = 33 # Local in function
    def nested():
        print(X) # Reference local in enclosing scope (33)

def h2():
    X = 33 # Local in function
    def nested():
        nonlocal X # Python 3.X statement
        X = 44 # Change local in enclosing scope

class Super:
    def hello(self):
        self.data1 = 'spam'

 class Sub(Super):
    def hola(self):
        self.data2 = 'eggs'

X = Sub()
X.__dict__
X.__class__
# Sub.

import example.class_examples.docstr as docstr
docstr.__doc__
docstr.fund.__doc__
docstr.spam.__doc__
docstr.spam.method.__doc__
x = docstr.spam()
x.__doc__
x.method()

help(docstr)