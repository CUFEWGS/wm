from pylab import mpl, plt

import matplotlib

import datetime as dt

dt.datetime.now()
dir(dt.datetime)

dt.MINYEAR
dt.MAXYEAR
today = dt.date(2019, 4, 25)
today.day
dt.tzinfo

#%% timedelta
from datetime import timedelta
year = timedelta(days = 365)
year.days

another_year = timedelta(weeks = 40, days = 84, hours = 23,
                         minutes = 50, seconds = 600)
year.total_seconds()
year == another_year
ten_years = year * 10
ten_years, ten_years.days // 365
nine_year = ten_years - year

nine_year.days // 365
nine_year, nine_year.days // 365
nine_year, nine_year.days // 365

three_years = nine_year // 3

three_years, three_years.days // 365

abs(three_years - ten_years) == 2 * three_years + year

#%% date
import time
from datetime import date
date.fromordinal(2019)
date.fromisoformat("2019-04-25")
date.resolution()
date.min
date.min
date.max
date.resolution

d = date(2002, 12, 31)
d.replace(day = 26)

date(2003, 12, 29).isocalendar()
date(2015, 1, 2).isocalendar()

date(2002, 12, 4).isoformat()
date(2002, 12, 4).__repr__()
date(2002, 12, 4).__str__()
help(dt.datetime.strptime)

dt.datetime.strptime("2019-04-02", "%Y-%m-%d")
date(2002, 12, 4).strftime("%y-%m-%d")

today = date.today()

my_birthday = date(today.year, 3, 24)
if my_birthday < today:
    my_birthday = my_birthday.replace(year = today.year + 1)

my_birthday

d = date.fromordinal(730920)
d
t = d.timetuple()
for i in t:
    print(i)

ic = d.isocalendar()
for i in ic:
    print(i)
d.isoformat()
d.strftime("%d/%m/%y")
d.strftime("%A %d. %B %Y")
print("The {1} is {0:%d}, the {2} is {0:%B}.".format(d, "day", "month"))