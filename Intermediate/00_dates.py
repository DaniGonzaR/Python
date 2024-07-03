### Dates ###

from datetime import datetime

now = datetime.now() # Obtains the current date and time

print(now.day)
print(now.month)
print(now.year)
print("-----")
print(now.hour)
print(now.minute)
print(now.second)

year_2024 = datetime(2024, 1, 1)

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print("-----")
print_date(year_2024)
print("-----")
from datetime import time
current_time = time() # Obtains the current time

from datetime import date
current_date = date.today() # Obtains the current date
print(current_date.year)
print(current_date.month)
print(current_date.day)
print("-----")

diff = year_2024 - now # Difference between two dates
print(diff)
print("-----")

from datetime import timedelta
start_timedelta = timedelta(200, 100, 100, weeks = 10)
end_timedelta = timedelta(300, 100, 100, weeks = 13)
print(start_timedelta - end_timedelta)
print(start_timedelta + end_timedelta)
