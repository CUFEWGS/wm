# -*- coding: utf-8 -*-
# @Time     : 2019/6/3 13:47
# @Author    ：Wang Guosong
# @File     : eg_managed_attributes.py
# @Software : PyCharm

# class Person:
#     def getName(self):
#         if not valid():
#             raise

attribute  =  property()

class Person:
    def __init__(self, name):
        self._name = name
    def getName(self):
        print('fetch ...')
        return self._name
    def setName(self, value):
        print('change ...')
        self._name = value
    def delNmae(self):
        print('remove ...')
        del self._name
    name = property(getName, setName, delNmae, 'name property docs')

bob = Person('Bob Smith')
print(bob.name)
bob.name = 'Robert Smith'
print(bob.name)
del bob.name

print('-' * 20)
sue = Person('Sue Jones')
print(sue.name)
print(Person.name.__doc__)

class PropSquare:
    def __init__(self, start):
        self.value = start
    def getX(self):
        return self.value ** 2
    def setX(self, value):
        self.value = value
    X = property(getX, setX)

P = PropSquare(3)
Q = PropSquare(32)

print(P.X)
P.X = 4
print(P.X)
print()

class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        "name property docs"
        print('fetch...')
        return self._name

    @name.setter
    def name(self, value):
        print('change...')
        self._name = value

    @name.deleter
    def name(self):
        print('remove...')
        del self._name

bob = Person('Bob Smith')
print(bob.name)
bob.name = 'Robert Smith'
print(bob.name)
del bob.name

print('-' * 20)
sue = Person('Sue Jones')
print(sue.name)
print(Person.name.__doc__)

class Name:
    "name descriptor docs"
    def __get__(self, instance, owner):
        print('fetch...')
        return instance._name
    def __set__(self, instance, value):
        print('change...')
        instance._name = value
    def __delete__(self, instance):
        print('remove...')
        del instance._name

class Person:
    def __init__(self, name):
        self._name = name
    name = Name()

bob = Person('Bob Smith')
print(bob.name)
bob.name = 'Robert Smith'
print(bob.name)
del bob.name

class DescBoth:
    def __init__(self, data):
        self.data = data
    def __get__(self, instance, owner):
        return '%s, %s' % (self.data, instance.data)
    def __set__(self, instance, value):
        instance.data = value

class Client:
    def __init__(self, data):
        self.data = data
    managed = DescBoth('spam')

I = Client('eggs')
I.managed
I.managed = 'SPAM'
I.managed

class DescSquare(object):
    def __get__(self, instance, owner):
        return instance._square ** 2
    def __set__(self, instance, value):
        instance._square = value

class DescCube(object):
    def __get__(self, instance, owner):
        return instance._cube ** 3

class Powers(object):
    square = DescSquare()
    cube = DescCube()
    def __init__(self, x, y):
        self._square = x
        self._cube = y

X = Powers(3, 4)
print(X.square)
print(X.cube)
X.square = 5
print(X.square)


class GetAttr:
    eggs = 88
    def __init__(self):
        self.spam = 77
    def __len__(self):
        print('__len__: 42')
        return 42
    def __getattr__(self, attr):
        print('getattr: ' + attr)
        if attr == '__str__':
            return lambda *args: '[Getattr str]'
        else:
            return lambda *args: None

class GetAttribute(object):
    eggs = 88
    def __init__(self):
        self.spam = 77
    def __len__(self):
        print('__len__: 42')
        return 42
    def __getattribute__(self, attr):
        if attr == '__str__':
            return lambda *args: '[GetAttribute str]'
        else:
            return lambda *args: None

# for Class in GetAttr, GetAttribute:
#     print('\n' + Class.__name__.ljust(50, "="))
#
#     X = Class()
#     X.eggs
#     X.spam
#     X.other
#     len(X)





