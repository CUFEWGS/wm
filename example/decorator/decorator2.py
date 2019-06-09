# -*- coding: utf-8 -*-
# @Time     : 2019/5/18 16:21
# @Author   ：Wang Guosong
# @File     : decorator2.py
# @Software : PyCharm

def tracer(func): # State via enclosing scope and nonlocal
    calls = 0 # Instead of class attrs or global
    def wrapper(*args, **kwargs): # calls is per-function, not global
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return wrapper

@tracer
def spam(a, b, c): # Same as: spam = tracer(spam)
    print(a + b + c)

if __name__ == '__main__':
    spam(1, 2, 3)  # Really calls wrapper, bound to func
    spam(a=4, b=5, c=6)  # wrapper calls spam