import empyrical
import pyfolio
import pandas as pd
import numpy as np

empyrical.calmar_ratio()
empyrical.sharpe_ratio()
pyfolio.create_full_tear_sheet()
pyfolio.create_full_tear_sheet()
pyfolio.risk()

data = pd.read_csv("D:/F/OSC/data/40165493_week_rows_51.csv",
            index_col=0,
            parse_dates=True,
            encoding='gbk')

ret = data['accum_nav'].pct_change()
ret_dropna = ret.dropna()

empyrical.annual_return(ret, period='weekly')
empyrical.annual_return(ret_dropna, period='weekly')

ann_factor = empyrical.stats.annualization_factor(period="weekly", annualization=None)
num_years = len(ret) / ann_factor
    # Pass array to ensure index -1 looks up successfully.
ending_value = empyrical.cum_returns_final(ret, starting_value=1)
np.prod(1 + ret) ** (52/50) - 1
len(ret)
len(ret.dropna())
dir(ret)
len()


prod(1 + ret)^(52/52) - 1

52 / 51
return ending_value ** (1 / num_years) - 1
empyrical.calmar_ratio()