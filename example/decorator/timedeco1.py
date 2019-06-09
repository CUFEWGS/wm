# -*- coding: utf-8 -*-
# @Time     : 2019/5/18 16:21
# @Author   ：Wang Guosong
# @File     : timedeco1.py
# @Software : PyCharm

import time, sys
force = list if sys.version_info[0] == 3 else (lambda X: X)

class timer:
    def __init__(self, func):
        self.func = func
        self.alltime = 0
    def __call__(self, *args, **kwargs):
        start = time.perf_counter()
        result = self.func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        self.alltime += elapsed
        print('%s: %.5f, %.5f' %(self.func.__name__, elapsed, self.alltime))
        return result

@timer
def listcomp(N):
    return [x * 2 for x in range(N)]

@timer
def mapcall(N):
    return force(map((lambda x: x * 2), range(N)))

result = listcomp(5)
listcomp(5000)
listcomp(50000)
listcomp(100000)
print(result)
print('allTime = %s' % listcomp.alltime)

print(' ')
result = mapcall(5)
mapcall(5000)
mapcall(50000)
mapcall(100000)
print(result)
print('allTime = %s' % mapcall.alltime)

print('\n **map/comp = %s' % round(mapcall.alltime / listcomp.alltime, 3))

def listcomp(N): [x * 2 for x in range(N)]
import timer
timer.total(1, listcomp, 100000)
import timeit
timeit.timeit(number=1, stmt=lambda : listcomp(1000000))