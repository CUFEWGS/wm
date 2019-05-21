# -*- coding: utf-8 -*-
# @Time     : 2019/5/18 16:21
# Author    ： Wang Guosong
# @File     : eg_sql_expression_language.py
# @Software : PyCharm

from jqdatasdk import *

from jqdata import finance

# from jqdata import finance
q = query(finance.STK_INCOME_STATEMENT).filter(
        finance.STK_INCOME_STATEMENT.code=='000783.XSHE',              #选定股票  000783.XSHE
        finance.STK_INCOME_STATEMENT.end_date > '2005-01-01',          #指定查询时间段大于2005年1月1日
        finance.STK_INCOME_STATEMENT.end_date < '2018-01-01',          #指定查询时间段小于2018年1月1日
        finance.STK_INCOME_STATEMENT.net_profit <0,                    #指定查询到的数据中net_profit为负
        finance.STK_INCOME_STATEMENT.report_type == 0,                 #指定报告期类型为本期
        ).order_by(finance.STK_INCOME_STATEMENT.end_date.desc()  ).limit(5)   #根据end_date降序排序,并返回前5条数据
finance.run_query(q)