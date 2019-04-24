# *_*coding:utf-8 *_*
from atrader import *
def init(context: Context):
    # 设置初始资金为100万
    set_backtest(initial_cash=1000000)
def on_data(context: Context):
    # 获取账户的持仓情况
    positions = context.account(account_idx=0).positions
    # 获取账户的资金情况
    cash = context.account(account_idx=0).cash
    # 买入开仓，市价委托
    order_volume(account_idx=0, target_idx=0, volume=1, side=1, position_effect=1, order_type=2)
if __name__ == '__main__':
    run_backtest(strategy_name='example_test', file_path='.', target_list=['shfe.rb0000'], frequency='min', fre_num=15, begin_date='2018-01-01', end_date='2018-06-30')