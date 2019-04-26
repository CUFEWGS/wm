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

# %% timedelta
from datetime import timedelta

year = timedelta(days=365)
year.days

another_year = timedelta(weeks=40, days=84, hours=23,
                         minutes=50, seconds=600)
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

# %% date
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
d.replace(day=26)

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
    my_birthday = my_birthday.replace(year=today.year + 1)

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

# %% datetime
from datetime import datetime
import time

dt.tzinfo
datetime.today()
datetime.fromtimestamp(time.time())
datetime.now()
datetime.utcnow()

from datetime import timezone

datetime.now(timezone.utc)
timezone.utc
datetime.max.toordinal()
d = datetime.now()
datetime.tzinfo
d.replace(tzinfo='US')
d - d.utcoffset()
datetime.utcfromtimestamp(time.time())

from datetime import tzinfo, timedelta, datetime


class TZ(tzinfo):
    def utcoffset(self, dt):
        return timedelta(minutes=-399)


datetime(2002, 12, 25, tzinfo=TZ()).isoformat(" ", "hours")
datetime(2002, 12, 25, tzinfo=TZ()).isoformat(" ", "milliseconds")

datetime.now().isoformat(timespec='minutes')
dt = datetime(2015, 1, 1, 12, 30, 59, 1)
dt.isoformat(timespec="microseconds")
dt.isoformat(timespec="milliseconds")

# examples
from datetime import datetime, date, time

# Using datetime.combine()
d = date(2019, 4, 25)
t = time(13, 40)
datetime.combine(d, t)
# Using datetime.now() or datetime.utcnow()
datetime.now()
datetime.utcnow()
# using datetime.strptime()
dt = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
dt
# Using datetime.timetuple() to get tuple of all attributes
tt = dt.timetuple()
for it in tt:
    print(it)

# Date in ISO format
ic = dt.isocalendar()
for it in ic:
    print(it)

# Formatting datetime
dt.strftime("%A, %d, %B %Y %I:%M%p")
'The {1} is {0:%d}, the {2} is {0:%B}, the {3} is {0:%I:%M%p}.'.format(dt, "day", "month", "time")


# Using datetime import timedelta, datetime, tzinfo
class GMT1(tzinfo):
    def utcoffset(self, dt):
        return timedelta(hours=1) + self.dst(dt)

    def dst(self, dt):
        # DST starts last Sunday in March
        d = datetime(dt.year, 4, 1)  # ends last Sunday in October
        self.dston = d - timedelta(days=d.weekday() + 1)
        d = datetime(dt.year, 11, 1)
        self.dstoff = d - timedelta(days=d.weekday() + 1)
        if self.dston <= dt.replace(tzinfo=None) < self.dstoff:
            return timedelta(hours=1)
        else:
            return timedelta(0)

        def tzname(self, dt):
            return "GMT +1"

class GMT2(tzinfo):
    def utcoffset(self, dt):
        return timedelta(hours = 2) + self.dst(dt)
    def dst(self, dt):
        d = datetime(dt.year, 4, 1)
        self.dston = d - timedelta(days = d.weekday() + 1)
        d = datetime(dt.year, 11, 1)
        self.dstoff = d - timedelta(days=d.weekday() + 1)
        if self.dston <= dt.replace(tzinfo = None) < self.dstoff:
            return timedelta(hours = 1)
        else:
            return timedelta(0)

    def tzname(self, dt):
        return "GMT +2"

gmt1 = GMT1()
# Daylight Saving Time
dt1 =  datetime(2006, 11, 21, 16, tzinfo = gmt1)

dt1.dst()
dt1.utcoffset()
dt2 = datetime(2006, 6, 14, 13, 0, tzinfo = gmt1)
dt2.dst()
dt2.utcoffset()

# Convert datetime to another time zone
dt3 = dt2.astimezone(GMT2())
dt2.utctimetuple() == dt3.utctimetuple()


#%% time
from datetime import time
time(hour = 12, minute = 34, second = 56, microsecond = 123456).isoformat(timespec = "minutes")
dt = time(hour = 12, minute = 34, second = 56, microsecond = 0)
dt.isoformat(timespec = "microseconds")
dt.isoformat(timespec = "auto")

dt1.tzname()

from datetime import time, tzinfo, timedelta

class GMT1(tzinfo):
    def utcoffset(self, dt):
        return timedelta(hours = 1)
    def dst(self, dt):
        return timedelta(0)
    def tzname(self, dt):
        return "Europe/Prague"

t = time(12, 20, 30, tzinfo = GMT1())
t
gmt = GMT1()
t.isoformat()
t.dst()
t.tzname()

t.strftime("%H:%M:%S %Z")
"The {} is {%H:%M}".format('time', t)

#%% tzinfo0
from datetime import tzinfo, timedelta, datetime

ZERO = timedelta(0)
HOUR = timedelta(hours = 1)
SECOND = timedelta(seconds = 1)

# A class capturing the platform's idea of local time.
# (May result in wrong values on historical times in
#  timezones where UTC offset and / or the DST rules had
# changed in the past.)

import time as _time

STDOFFSET = timedelta(seconds = -_time.timezone)
if _time.daylight:
    DSTOFFSET = timedelta(seconds = -_time.altzone)
else:
    DSTOFFSET = STDOFFSET

DSTDIFF = DSTOFFSET - STDOFFSET

class LocalTimezone(tzinfo):

    def fromutc(self, dt):
        assert dt.tzinfo is self
        stamp = (dt - datetime(1970, 1, 1, tzinfo = self)) // SECOND
        args = _time.localtime(stamp)[:6]
        dst_diff = DSTDIFF // SECOND
        #Detect fold
        fold  = (args == _time.localtime(stamp - dst_diff))
        return  datetime(*args, microseconds = dt.microsecond,
                         tzinfo = self,
                         fold = fold)

    def utcoffset(self, dt):
        if self._isdst(dt):
            return DSTOFFSET
        else:
            return STDOFFSET

    def dst(self, dt):
        if self._isdst(dt):
            return DSTDIFF
        else:
            return ZERO

    def tzname(self, dt):
        return _time.tzname[self._isdst(dt)]

    def isdst(self, dt):
        tt =  (dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, dt.weekday(), 0, 0)
        stamp = _time.mktime(tt)
        tt = _time.localtime(stamp)
        return tt.tm_isdst > 0

Local = LocalTimezone()

# A complete implementation of current DST rules for major US time zones.

def first_sunday_on_or_after(dt):
    days_to_go = 6 - dt.weekday()
    if days_to_go:
        dt += timedelta(days_to_go)

    return dt

#%% strftime() strptime()

date(2019, 1, 7).__format__("%c")

