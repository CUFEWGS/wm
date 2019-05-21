# -*- coding: utf-8 -*-
# @Time     : 2019/5/21 20:10
# Author    ： Wang Guosong
# @File     : eg_quick_pd.py
# @Software : PyCharm

import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8])

dates = pd.date_range('20190520', periods=6)
dates = pd.date_range('2019-05-20', periods=6)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

df2 = pd.DataFrame({'A' : 1.,
                    'B' : pd.Timestamp('20130102'),
                    'C' : pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D' : np.array([3] * 4, dtype='int32'),
                    'E' : pd.Categorical(['test', 'train', 'test', 'train']),
                    'F' : 'foo'})


df.dtypes
df2.dtypes

df2.abs
df2.head()
df.tail(3)

df.index

df2.columns
df2.to_numpy()

df.describe()
df.T
df.sort_index(axis=1, ascending=False)
df.sort_values(by='B')

df['A']
df[0:3]
df.loc[dates[0]]
df.loc[:, ['A', 'B']]
df.at[dates[0], 'A']

df.iloc[3]
df.iloc[3:5, 0:2]
df.iloc[[1, 2, 4], [0, 2]]
df.iloc[1:3, :]
df.iloc[:, 1:3]

df.iloc[1, 1]
df.iat[1, 1]

df[df.A > 0]
df[df > 0]

df3 = df.copy()
df3['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
df3
df
df3[df3['E'].isin(['two', 'four'])]

s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20190519', periods=6))
s1
df['F'] = s1
df

df.at[dates[0], 'A'] = 0
df.iat[0, 1] = 1
df.iloc[0, 1] = 0

df.loc[:, 'D'] = np.array([5] * len(df))
df.loc[:, 'D'] = [5] * len(df)

df2 = df.copy()
df2[df2 > 0] = -df2
