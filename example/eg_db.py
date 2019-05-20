# -*- coding: utf-8 -*-
# @Time     : 2019/5/19 17:31
# Author    ： Wang Guosong
# @File     : eg_db.py
# @Software : PyCharm

import pandas as pd
from sqlalchemy import create_engine

engine_dys = create_engine('oracle+cx_oracle://cfgl_cfyj:cfgl_cfyj123@10.45.5.21:1521/sjcj')


engine = create_engine('sqlite:///D:/E/Python/sqlite_test/test1', echo=True)

conn = engine_dys.connect()