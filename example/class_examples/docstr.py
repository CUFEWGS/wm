# -*- coding: utf-8 -*-
# @Time     : 2019/5/27 11:22
# Author    ：Wang Guosong
# @File     : docstr.py
# @Software : PyCharm

"I am: docstr.__doc__"


def func(args):
    "I am: docstr.fund.__doc__"
    padd


class spam:
    "I am: spam.__doc__ or docstr.spam.__doc__ or self.__doc__"
    def method(self):
        "I am: spam.method.__doc__ or self.method.__doc__"
        print(self.__doc__)
        print(self.method.__doc__)