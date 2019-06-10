# -*- coding: utf-8 -*-
# @Time     : 2019/6/9 13:18
# @Author   ：Wang Guosong
# @File     : date_util.py
# @Software : PyCharm

from bizdays import Calendar, load_holidays
import re
from datetime import datetime, date

class DateUtil():
    """
    DateUtil is for date switch.
    """

    def __init__(self):
        self.holidays = load_holidays('docs/china_cal.txt')
        self.cal = Calendar(self.holidays, ['Sunday', 'Saturday'])


    def floor_date(self, dt, unit):
        """
        Parameters
        ----------
        dt :
        unit :

        Returns
        -------

        Examples
        -------
        """

    # @staticmethod
    def __add_date_floor_ceil(self, dt, date_rule):
        """

        Parameters
        ----------
        dt : date, string of ISO format
            date to be offset
        date_rule : string
            expression of date rule

        Returns
        -------

        Examples
        -------
        dt = '2019-06-09'
        date_rule = '_fd'
        date_rule = '_zd'

        """
        m = re.match('^_(f|c)[a-z]$', date_rule)
        if not isinstance(m, re.Match):
            raise TypeError("date rule must be '_fX' or '_lX',"
                            " where X is one of d,w,m,b,q,h,y")
        op = m[0][1:2]
        unit = m[0][2:3]

        switch = {'f': 'first week', 'l': 'last week'}

        dt_date = date.fromisoformat(dt)

        self.cal.getdate(switch[op], dt_date.year, dt_date.month)





