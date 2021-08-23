# Importing modules using from
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
import calendar
# A timedelta object represents a duration, the difference between two dates or times.
# https://docs.python.org/3/library/datetime.html
#print(date.today())

#print(datetime.now())

# format date and time

def main1():
  now = datetime.now()
  print(now.strftime("%Y-%A-%B"))
  print(now.strftime("%y-%a-%b"))
  year = timedelta(days=365)
  another_year = timedelta(weeks=40, days=83, hours=23,minutes=50, seconds=600)
  print (year == another_year)
  #print(timedelta(days=365,hours=5,minutes=1))
  t = year - another_year
  print(t)
  c = calendar.TextCalendar(calendar.THURSDAY)
  st = c.formatmonth(2021,8,0,0)
  print(st)

def main():
  for name in calendar.month_name:
    print(name)
  for day in calendar.day_name:
    print(day)

def monthCalender():
  for m in range(1,3):
    cal = calendar.monthcalendar(2021,m)


if __name__ == "__main__":
  main()
