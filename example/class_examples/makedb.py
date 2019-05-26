# -*- coding: utf-8 -*-
# @Time     : 2019/5/26 19:10
# Author    ：Wang Guosong
# @File     : makedb.py
# @Software : PyCharm

from example.class_examples.person import Person, Manager
bob = Person('Bob Smith')
sue = Person('Sue Jones', job='dev', pay=10000)
tom = Manager('Tom Jones', 50000)

import shelve
db = shelve.open('persondb')
for obj in (bob, sue, tom):
    db[obj.name] = obj
db.close()

import glob
glob.glob('person*')
print(open('persondb.dir').read())

import shelve
db = shelve.open('persondb')
len(db)
list(db.keys())
bob = db['Bob Smith']
bob
bob.lastName()

for key in db:
    print(key, '=>', db[key])

for key in sorted(db):
    print(key , '=>', db[key])