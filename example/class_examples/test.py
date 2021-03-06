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

L = [5, 6, 7, 8, 9]
L[slice(2, 4)]

L[2:4]

class Indexer:
    def __getitem__(self, index):
        if isinstance(index, int):
            print('indexing', index)
        else:
            print('slicing', index.start, index.stop, index.step)

X = Indexer()
X[99]
X[1:99:2]
X[1:]

class Squares:
    def __init__(self, start, stop): # Save state when created
        self.value = start - 1
        self.stop = stop

    def __iter__(self): # Get iterator object on iter
        return self

    def __next__(self): # Return a square on each iteration
        if self.value == self.stop: # Also called by next built-in
            raise StopIteration
        self.value += 12

for i in Squares(1, 5):
    print(i, end=' ')

class C1:
    def meth1(self): self.__X = 88 # I assume X is mine
    def meth2(self): print(self.__X)

class C2:
    def metha(self): self.__X = 99 # Me too
    def methb(self): print(self.__X)


class C3(C1, C2): ...
I = C3()
I.meth2()
I.metha()
I.methb()
print(I.__dict__)

class Number:
    def __init__(self, base):
        self.data = base
    def double(self):
    return self.data * 2
    def triple(self):
        return self.data * 3

x = Number(2)
x.double()

bound = x.double
bound
bound.__self__
bound.__func__
bound.__self__.data
bound()

class Spam:
    def __init__(self):
        self.data1 = "food"
X = Spam()
print(X)


from example.class_examples.setwrapper import Set
x = Set([1, 3, 5, 7])
print(x.union(Set([1, 4, 7])))
print(x | Set([1, 4, 6]))

from example.class_examples.spam import Spam
a  = Spam()
b = Spam()
c = Spam()
Spam.printNumInstances()
a.printNumInstances()


def printNumInstances():
    print("Number of instances created: %s" % Spam.numInstances)

class Spam:
    numInstances = 0

    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1

a = Spam()
b = Spam()
c = Spam()
printNumInstances()

from example.class_examples.bothmethod import Methods
obj = Methods()
obj.imeth(1)
Methods.imeth(obj, 2)
# Methods.imeth(2)
Methods.smeth(3)
obj.semth(4)
Methods.smeth1(3)
obj.smeth1(4)

Methods.cmeth(5)
obj.cmeth(6)

class Spam:
    numInstances = 0 # Trace class passed in
    def __init__(self):
        Spam.numInstances += 1
    def printNumInstances(cls):
        print("Number of instances: %s %s" % (cls.numInstances, cls))
        a = 1
        return a
    printNumInstances = classmethod(printNumInstances)
    def test(self):
        self.x = printNumInstances()


class Sub(Spam):
    def printNumInstances(cls): # Override a class method
        print("Extra stuff...", cls) # But call back to original
        Spam.printNumInstances()
    printNumInstances = classmethod(printNumInstances)

class Other(Spam): pass # Inherit class method verbatim

x = Sub()
y = Other()
y.printNumInstances()


def generate():
    class Spam: # Spam is a name in generate's local scope
        count = 1
        def method(self):
            print(Spam.count) # Visible in generate's scope, per LEGB rule (E)
    return Spam()

generate().method()

class C:
    # __slots__ = ['B']
    pass

class D(C):
    __slots__ = ['a']

C.__dict__.keys()
D.__dict__.keys()

X = D()
X.a = 1
X.b = 1

class operators:
    def __getattr__(self, name): # On undefined reference
        if name == 'age':
            return 40
        else:
            raise AttributeError(name)

    def __setattr__(self, name, value): # On all assignments
        print('set: %s %s' % (name, value))
        if name == 'age':
            self.__dict__['_age'] = value # Or object.__setattr__()
        else:
            self.__dict__[name] = value

x = operators()
x.age
x.age = 41
x._age