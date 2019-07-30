# -*- coding: utf-8 -*-
# @Time     : 2019/5/18 16:21
# @Author   ：Wang Guosong
# @File     : eg_timing.py
# @Software : PyCharm

import timer

X = 99

def sector():
    print(X)
    X = 88


sector()

L = [1, 2, 3]
L.append(4)
print(L)

t = list([1, 2, 3]).append([4])
z = [1, 2, 3]
z.append(1)
z.append(2)
z