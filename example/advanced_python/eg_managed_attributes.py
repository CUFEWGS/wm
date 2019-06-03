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

class Person:
    def __init__(self, name):
        self.name = name
    def __getattr__(self, attr):
        print('get:' + attr)
        if attr == 'name':
            return self._name
        else:
            raise AttributeError(attr)

    def __setattr__(self, attr, value):
        print('set:' + attr)
        if attr == 'name':
            attr = 'name'
        self.__dict__[attr] = value

    def __delattr__(self, attr):
        print('del:' + attr)
        if attr == 'name':
            attr = '_name'
        del self.__dict__[attr]

bob = Person('Bob Smith')
print(bob.name)
bob.name = 'Robert Smith'

class AttrSquare: # Add (object) for 2.X
    def __init__(self, start):
        self.value = start # Triggers __setattr__!

    def __getattribute__(self, attr): # On all attr fetches
        if attr == 'X':
            return self.value ** 2 # Triggers __getattribute__ again!
        else:
            return object.__getattribute__(self, attr)

    def __setattr__(self, attr, value): # On all attr assignments
        if attr == 'X':
            attr = 'value'
        object.__setattr__(self, attr, value)

A = AttrSquare(3) # 2 instances of class with overloading
B = AttrSquare(32) # Each has different state information
print(A.X) # 3 ** 2
A.X = 4
print(A.X) # 4 ** 2
print(B.X) # 32 ** 2 (1024)