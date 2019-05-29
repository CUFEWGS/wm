# -*- coding: utf-8 -*-
# @Time     : 2019/5/29 14:03
# Author    ：Wang Guosong
# @File     : spam.py
# @Software : PyCharm


class Spam:
    numInstances = 0

    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1

    def printNumInstances():
        print("Number of instances created: %s" % Spam.numInstances)