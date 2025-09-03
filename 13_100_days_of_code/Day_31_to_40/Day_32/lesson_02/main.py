
# datetime module

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()


print(year)
print(month)
print(day)
print(day_of_week)


date_of_birth = dt.datetime(year=1999, month=8, day=20, hour=15)
print(date_of_birth)