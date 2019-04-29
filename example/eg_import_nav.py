import pandas as pd
import numpy as np
import os
import itertools

cwd = os.getcwd()
path = "example\黑逸数据分析.xlsx"

data = pd.read_excel(path, parse_dates = True)
data = pd.read_excel(path, dtype = {'日期': str}, skiprows = 1)
# data1 = pd.read_excel(path)
# data

pd.read_excel(path)
# del(data)
data.head(15)
test = data.tail()
_
data.describe()

data.pipe(pd.describe())

data.aggregate(['sum', 'min'])

help(data)

help(pd.read_excel)
help(data.tail)

range

np.arange()
range()
