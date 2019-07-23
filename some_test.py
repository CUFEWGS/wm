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