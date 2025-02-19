
import datetime as dt

now=dt.datetime.now()
print(now)
year=now.year
month=now.month
day_of_week =now.weekday()
print(day_of_week)

date_of_birth=dt.datetime(year=1990,month=11,day=11,hour=7)
print(date_of_birth)
