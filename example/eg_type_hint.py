# -*- coding: utf-8 -*-
# @Time     : 2019/5/22 10:26
# Author    ： Wang Guosong
# @File     : type_hint.py
# @Software : PyCharm

class C:
    foo = None # type: List[str]

    def __init__(self, bar):
        self.bar = bar # type: Optional[str]

        def f2():
            return 'foo'

        def f1():
            x = f2() # type: str
            return x.upper()

from typing import List, Optional

xs: List[Optional[str]] = []