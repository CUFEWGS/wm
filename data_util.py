# -*- coding: utf-8 -*-
# @Time     : 2019/5/22 9:07
# Author    ： Wang Guosong
# @File     : data_util.py
# @Software : PyCharm

import pandas as pd


class DataUtil:
    """
    test
    """

    @staticmethod
    def df_to_series():
        """
        :param df: a DataFrame with the first column of datetime or something like that
        :return series: a Series that value is the last column
        """
        # series = pd.Series(df.iloc[:, -1], name='value')
        # series.index = pd.to_datetime(df.iloc[:,0])
        # # series = pd.Series(df.iloc[:, -1], index=pd.to_datetime(df.iloc[:, 0]))

        # series = series.set_axis(pd.to_datetime(df.iloc[:, 0], infer_datetime_format=True), labels="date")
        # series.sort_index(inplace=True)
        # return series
        return 2

# import numpy as np
# np.array()
#
# tes
# pd.to_datetime(df.iloc[:, 0], format="%Y%M%d")
#
# if __name__ == '__main__':
#     import