# -*- coding: utf-8 -*-
# @Time     : 2019/5/18 16:21
# Author    ：Wang Guosong
# @File     : eg_class.py
# @Software : PyCharm

class C2:
    pass

class C3:
    pass

class C1(C2, C3):
    def setname(self, who):
        self.name = who

I1 = C1()
I2 = C1()
I1.setname('bob')
I2.setname('sue')
print(I1.name)

class C2():
    def __init__(self, who): # attribute here is always set
        self.name = who

class C1(C2, C3):
    pass
I3 = C1('BOB')
class Employee:
    def computeSalary(self):
        pass

    def giveRaise(self):
        padd

    def promote(self):
        pass

    def retire(self):
        pass

class Engineer(Employee):
    def computeSalary(self):
        pass

bob = Employee()
sue = Employee()
tom = Engineer()
company = [bob, sue, tom]
for emp in company:
    print(emp.computeSalary())

class FirstClass:
    def setdata(self, value):
        self.data = value

    def display(self):
        print(self.data)

x = FirstClass()
y = FirstClass()
x.setdata('King Arthur')
y.setdata(3.14159)
x.data
x.data = 'New Value'
x.display()

class SecondClass(FirstClass):
    def display(self):
        print('Current value =  "%s" ' % self.data)

z = SecondClass()
z.setdata(42)
z.display()

# from eg_class import FirstClass

class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value
    def __add__(self, other):
        return ThirdClass(self.data + other)
        return ThirdClass(self.data + other)
    def __str__(self):
        return '[ThirdClass: % s]' % self.data
    def mul(self, other):
        self.data *= other

a = ThirdClass('abc')
a.display()
print(a)
b = a + 'xyz'
b.display()
print(b)
a.mul(3)
print(a)

class rec:
    pass

rec.name = 'Bob'

x = rec()
y = rec()
x.name
list(rec.__dict__.keys())
x.__dict__['name']
rec.__class__
rec.__bases__

def uppername(obj):
    return obj.name.upper()

uppername(x)

rec.method = uppername
x.method()
y.method()

class Person:
    def __init__(self, name, jobs, age=None):
        self.name = name
        self.jobs = jobs
        self.age = age

    def info(self):
        return (self.name, self.jobs)