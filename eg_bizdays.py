# -*- coding: utf-8 -*-
# @Time     : 2019/6/9 15:25
# @Author   ：Wang Guosong
# @File     : eg_bizdays.py
# @Software : PyCharm

from bizdays import Calendar, load_holidays

holidays = load_holidays('docs/china_cal.txt')
cal = Calendar(holidays, ['Sunday', 'Saturday'])
# cal = Calendar(holidays=['2019-06-07'])
cal.isbizday('2019-06-09')
cal.isbizday('2019-06-10')
cal.bizdays('2019-01-01', "2019-06-09")
cal.adjust_next('2019-06-09')
cal.adjust_previous('2019-06-09')
list(cal.seq('2019-04-01', "2019-06-09"))
cal.offset('2019-06-05', 2)
cal.offset('2019-06-05', -2)
cal.getdate('15th day', 2019, 6)
cal.getdate('15th bizday', 2019, 6)
cal.getdate('last wed', 2019, 5)
cal.getdate('first fri before last day', 2019, 6)
cal.getdate('first fri before last bizday', 2019, 6)
cal.getdate('first fri before last bizday', 2019, 6)
cal.following('2019-06-09')
cal.preceding('2019-06-09')

#%% modified_following & modified preceding

dt = cal.getdate('first day', 2019, 5)
# cal.modified_following(dt, iso=True)
cal.preceding(dt, iso=True)
cal.modified_preceding(dt, iso=True)

dt = cal.getdate('last day', 2019, 3)
cal.following(dt, iso=True)
cal.modified_following(dt, iso=True)
# cal.modified_preceding(dt, iso=True)

## attention
cal.offset('2019-06-09', 1)
cal.offset('2019-06-09', 0)
