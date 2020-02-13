# time usefull for working with epoch timestamp,
# but for doign arithmetic with dates or just displaying the date in a convenient format use datetime

import datetime
import time
# can't use datetime filename while importing datetime!

# return tuple with current date info
print(datetime.datetime.now())

# retrieve datetime object from specific time
date = datetime.datetime(2019, 10, 21, 16, 29, 0)
print(
    f'New date object:\t{date.day}-{date.month}-{date.year} \nwith time of:\t\t{date.hour}:{date.minute}')

# return datetime object from epoch timestamp
print(datetime.datetime.fromtimestamp(time.time()))

# can use comparison operator between different datetime objects
halloween2020 = datetime.datetime(2019, 10, 31, 0, 0, 0)
newyears2021 = datetime.datetime(2020, 1, 1, 0, 0, 0)
if halloween2020 < newyears2021:
    print(f'Halloween 2020 is {newyears2021 - halloween2020} days before new years 2021')
    print()

# timedelta represents a duration of time rather than a moment in time
# create a duration of time aka delta
delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days)
print(delta.seconds)
# total seconds in delta
print(delta.total_seconds())

# convert back to a string
print(str(delta))

# timedelta can be used for arithmetic operation on datetime object
dt = datetime.datetime.now()
thousandDays = datetime.timedelta(days=1000)
thousandDaysFromNow = dt + thousandDays
print(thousandDaysFromNow)

oct21st = datetime.datetime(2020, 10, 21, 16, 29, 0)
aboutThirtyYears = datetime.timedelta(days=365 * 30)
aboutThirtyYearsFromOct21st = oct21st + aboutThirtyYears
print(aboutThirtyYearsFromOct21st)

# pause program every second to save CPU processing cycles
halloween2020 = datetime.datetime(2020, 10, 31, 0, 0, 0)
while datetime.datetime.now() < halloween2020:
    time.sleep(1)
    
    # break otherwise program will keep running untill halloween 2020
    break
