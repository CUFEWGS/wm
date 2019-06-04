# -*- coding: utf-8 -*-
# @Time     : 2019/6/4 17:05
# @Author    ：Wang Guosong
# @File     : validate_tester.py
# @Software : PyCharm

from __future__ import print_function

def loadclass():
    import sys, importlib
    modulename = sys.argv[1]
    module = importlib.import_module(modulename)
    print('[Using: %s]' % module.CardHolder)

def printholder(who):
    print(who.acct, who.name)