# -*- coding: utf-8 -*-
# @Time     : 2019/5/28 19:04
# Author    ：Wang Guosong
# @File     : setwrapper.py
# @Software : PyCharm

class Set:
    def __init__(self, value = []):
        self.data = []
        self.concat(value)

    def interset(self, other):
        res = []
        for x in self.data:
            if x in other:
                res.append(x)
        return Set(res)

    def union(self, other):
        res = self.data[:]
        for x in other:
            if not x in res:
                res.append(x)
        return Set(res)

    def concat(self, value):
        for x in value:
            if not x in self.data:
                self.data.append(x)

    def __len__(self): return len(self.data)

    def __getitem__(self, key): return self.data[key]

    def __and__(self, other): return self.interset(other)

    def __or__(self, other): return self.union(other)

    def __repr__(self): return 'Set:' + repr(self.data)

    def __iter__(self): return iter(self.data)





