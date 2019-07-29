# -*- coding: utf-8 -*-
# @Time     : 2019/7/23 19:43
# @Author    ：Wang Guosong
# @File     : some_test.py
# @Software : PyCharm

import pandas as pd
import numpy as np
import string

df = pd.DataFrame(np.random.random(100).reshape([20, 5]), columns=list(string.ascii_lowercase[0:5]))
len(df)

df = pd.DataFrame(np.random.random(100).reshape([5, 20]), columns=list(string.ascii_lowercase[0:20]))
len(df)

def test_name():
    print([i for i in range(10000000)])

test_name()
a = test_name
a()


list(filter((lambda x: x > 0), range(-5, 5)))

M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

N = [[2, 2, 2],
     [3, 3, 3],
     [4, 4, 4]]


[[M[row][col] * N[row][col] for col in range(3)] for row in range(3)]


def gen(N):
    for i in range(N):
        # return i ** 2
        yield i ** 2

for i in gen(5):
    print(i, end=':')

test = (x + '\n' for x in 'aaa, bbb, ccc'.split(','))
test
a, b, c= (x + '\n' for x in 'aaa, bbb, ccc'.split(','))
a, b, c = test
a


G = (c * 4 for c in 'SPAM')
G
next(G)
I = iter(G)
next(I)

line = 'aa bbb c'

def gensub(line):
    for x in line.split():
        if len(x) > 1:
            yield x.upper()

''.join(gensub(line))

def retsub(line):
    for x in line.split():
        if len(x) > 1:
            return x.upper()

''.join(retsub(line))

