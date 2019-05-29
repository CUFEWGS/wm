# -*- coding: utf-8 -*-
# @Time     : 2019/5/29 15:15
# Author    ：Wang Guosong
# @File     : bothmethod.py
# @Software : PyCharm


class Methods:

    def imeth(self, x):
        print([self, x])

    def smeth(x):
        print([x])

    def smeth1(x):
        print([x])

    def cmeth(cls, x):
        print([cls, x])

    semth = staticmethod(smeth)
    cmeth = classmethod(cmeth)