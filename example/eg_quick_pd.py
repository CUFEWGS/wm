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

df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])

df1.loc[dates[0]:dates[1], 'E'] = 1
df1.dropna(how='any')
df1.fillna(value=5)

pd.isna(df1)

df.mean()
df.mean(1)

s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
df
df.sub(s, axis='index')

df.apply(np.cumsum)
df.apply(lambda x: x.max() - x.min())

s = pd.Series(np.random.randint(0, 7, size=10))
s.value_counts()

s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', 'np.nan', 'CABA', 'DOG', 'cat'])
s.str.lower()

df = pd.DataFrame(np.random.randn(10, 4))
pieces = [df[:3], df[3:7], df[7:]]
pd.concat(pieces)

left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
pd.merge(left, right, on='key')
left.merge(right, on='key')

df = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])
s = df.iloc[3]
df.append(s, ignore_index=True)

df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
                         'foo', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'two', 'three',
                         'two', 'two', 'one', 'three'],
                   'C': np.random.randn(8),
                   'D': np.random.randn(8)})

df.groupby('A').sum()
df.groupby(['A', 'B']).sum()

tuples = list(zip(*[['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
                    ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]))
tuples
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
df2 = df[:4]
stacked = df2.stack()

stacked.unstack()
stacked.unstack(0)

df = pd.DataFrame({'A': ['one', 'one', 'two', 'three'] * 3,
                   'B': ['A', 'B', 'C'] * 4,
                   'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                   'D': np.random.randn(12),
                   'E': np.random.randn(12)})

pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'])

rng = pd.date_range('1/1/2019', periods=10000, freq='S')
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
ts.resample('5Min').last()

rng = pd.date_range('3/6/2019 0:00', periods=5, freq='D')
ts = pd.Series(np.random.randn(len(rng)), rng)
ts
ts_utc = ts.tz_localize('UTC')
ts_utc.tz_convert('US/Eastern')

rng = pd.date_range('3/6/2019 0:00', periods=5, freq='M')
ts = pd.Series(np.random.randn(len(rng)), rng)
ts.to_period()
ts_utc.to_period().to_timestamp()

prng = pd.period_range('1990Q1', '2000Q4', freq='Q-NOV')
ts = pd.Series(np.random.randn(len(prng)), prng)
ts.index = (prng.asfreq('M', 'e') + 1).asfreq('H', 's') + 9

df = pd.DataFrame({"id": [1, 2, 3, 4, 5, 6],
                   "raw_grade": ['a', 'b', 'b', 'a', 'a', 'e']})
df["grade"] = df["raw_grade"].astype("category")
df["grade"].cat.categories = ["very good", "good", "very bad"]
df["grade"] = df["grade"].cat.set_categories(["very bad", "bad", "medium",
                                              "good", "very good"])
df.sort_values(by="grade")
df.groupby('grade').count()

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()
from matplotlib.pylab import plt
plt.show()

df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index,
                  columns=['A', 'B', 'C', 'D'])

df = df.cumsum()
plt.figure()
df.plot()
plt.show()
plt.legend(loc='best')

df.to_hdf('foo.h5', 'df')

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['a', 'b', 'c'])
df.to_hdf('data.h5', key='df', mode='w')