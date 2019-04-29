import numpy as np
import pandas as pd
from pylab import mpl, plt
# import matplotlib.pyplot as plt

plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'
# %matplotlib inline
plt.show()
# help(plt.style.use
# ('seaborn'))
# plt.style.available

file_path = "example/XX_CTA策略-20190404.csv"
f = open(file_path, 'r')
f.readlines()[:5]

data = pd.read_csv(file_path,
                   index_col=0,
                   parse_dates=True,
                   encoding='gbk')
                   # dtype={'回撤': np.float64, '日涨跌': np.float64})

data.info()
data.head()
data.tail()
# data['CTA净值'].plot(figsize = (10, 12))
data.plot(figsize = (10, 12), subplots=True)
data.describe().round(2)
data.mean()
data['CTA净值'].aggregate([min, np.mean, np.std, np.median, max])
data.aggregate([min, np.mean, np.std, np.median, max]).round(2)
data.head()
data.info()
data.drop(columns = ['回撤', '日涨跌', 'Unnamed: 6',  'Unnamed: 7']).diff().head()
data.drop(columns = data.columns[3:6]).diff().head()
data.drop(data.columns[3:6], axis = 1).diff().head()
data.drop(data.columns[1:2], axis = 1).diff().head()
data.drop(data.columns[[1,3]], axis = 1)
data.iloc[:, 1:4].diff().head()
data.iloc[:, [1,3]]

data.drop(columns = ['Unnamed: 6',  'Unnamed: 7']).dropna().diff().head()
data.diff()


data.iloc[:, 0:3].pct_change().round(3).head()
data.iloc[:, 0:3].pct_change().mean().plot(kind = 'bar', figsize = (10, 6))
plt.show()
rets = np.log(data.iloc[:, 0:3] / data.iloc[:, 0:3].shift(1))
rets.head().round(3)
rets.cumsum().apply(np.exp).plot(figsize = (10, 6))
plt.show()
data.iloc[:, 0:3].pct_change().cumsum().apply(np.exp).plot(figsize = (10, 6))

data.resample('1w', label = 'right').last().head()
data.resample('1m', label = 'right').last().head()
rets.cumsum().apply(np.exp).resample('1m', label = 'right').last().plot(figsize = (10, 6))
plt.show()

#%% rolling statistics
data.head()

sym = 'CTA净值'
data = pd.DataFrame(data[sym].dropna())

window = 20
data['min'] = data[sym].rolling(window= window).min()
data.head()
data['mean'] = data[sym].rolling(window = window).mean()
data['std'] = data[sym].rolling(window = window).std()
data['median'] = data[sym].rolling(window = window).median()
data['max'] = data[sym].rolling(window = window).max()
data['ewma'] = data[sym].ewm(halflife=0.5, min_periods=window).mean()

ax = data[['min', 'mean', 'max']].iloc[-200:].plot(
    figsize = (10, 6), style = ['g--', 'r--', 'g--'], lw = 0.8)
data[sym].iloc[-200:].plot(ax = ax, lw = 2.0)
plt.show()

data['SMA1'] = data[sym].rolling(window = 42).mean()
data['SMA2'] = data[sym].rolling(window = 252).mean()
data[[sym, 'SMA1', 'SMA2']].tail()

data[[sym, 'SMA1', 'SMA2']].plot(figsize = (10, 6))
plt.show()

data.dropna(inplace=True)
data['positions'] = np.where(data['SMA1'] > 1.15 * data['SMA2'], 1, -1)
ax = data[[sym, 'SMA1', 'SMA2', 'positions']].plot(figsize = (10, 6),
                                                   secondary_y = 'positions')
ax.get_legend().set_bbox_to_anchor((0.25, 0.85))
plt.show()


#%% correlation analysis
raw = pd.read_csv(file_path, index_col = 0, parse_dates=True, encoding='gbk')
data = raw[['CTA净值', '中证500']].dropna()
data.plot(subplots = True, figsize = (10, 6))
plt.show()

data.loc[: '2018-12-31'].plot(secondary_y = '中证500', figsize = (10, 6))
plt.show()
rets = np.log(data / data.shift(1))
rets.head()
rets.dropna(inplace = True)
rets.plot(subplots = True, figsize = (10, 6))
plt.show()
pd.plotting.scatter_matrix(rets,
                            alpha = 0.2,
                            diagonal = 'hist',
                            hist_kwds = {'bins': 35},
                            figsize = (10, 6)
                            )

#%% OLS regression
reg = np.polyfit(rets['CTA净值'], rets['中证500'],deg= 1)
ax = rets.plot(kind = 'scatter', x = 'CTA净值', y = '中证500', figsize = (10, 6))
ax.plot(rets['CTA净值'], np.polyval(reg, rets['中证500']), 'r', lw = 2)

rets.corr()
ax = rets['CTA净值'].rolling(window = 252).corr(
                    rets['中证500']).plot(figsize = (10, 6))
ax.axhline(rets.corr().iloc[0, 1], c = 'r')
plt.show()

#%% High Frequency Data
import timeit
# # data from example of tick data of 平安银行 20190429
# timeit.timeit("tick = pd.read_csv('example/payh_tick_data20190429.csv', skiprows = 1,
#        index_col = 0, parse_dates = True, encoding='gbk')")

tick = pd.read_csv("example/payh_tick_data20190429.csv", skiprows = 2,
       index_col = 0, parse_dates = True, encoding='gbk')

tick.info()
tick.head()
tick['Mid'] = tick.mean(axis = 1)
tick['Mid'].plot(figsize = (10, 6))
plt.show()

tick_resam = tick.resample(rule = "5min", label = 'right').last()
tick_resam['Mid'].plot(figsize = (10, 6))
plt.show()