### Dates ###

from datetime import datetime

now = datetime.now()
def print_date(date):
  print(date.day)
  print(date.hour)
  print(date.minute)
  print(date.second)
  print(date.year)
  print(date.month)
  print(date.timestamp())

print_date(now)
timestamp = now.timestamp()  
print(timestamp)

year_2023 = datetime(2023, 1, 1, 1, 1, 1)

print(year_2023)


from datetime import time

currenn_time = time(21, 6, 0)

print(currenn_time.hour)
print(currenn_time.minute)
print(currenn_time.second)


from datetime import date
currenn_date = date.today()

print(currenn_date.year)
print(currenn_date.month)
print(currenn_date.day)

currenn_date = date(2022, 10, 6)
print(currenn_date.year)
print(currenn_date.month)
print(currenn_date.day)

currenn_date = date(currenn_date.year, currenn_date.month + 1, currenn_date.day )

print(currenn_date.month)

diff = year_2023 - now
diff1 = year_2023.date() - currenn_date
print(diff)
print(diff1)
print(year_2023.time())

from datetime import timedelta

star_timedelta = timedelta(200, 100, 100, weeks= 10)
end_timedelta = timedelta(300, 100, 100, weeks= 13)

print(end_timedelta - star_timedelta)
print(end_timedelta + star_timedelta)
print(end_timedelta / star_timedelta)

