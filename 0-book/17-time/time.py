import time

# date of epoch
print(time.gmtime(0))

# epoch aka seconds since begining 1970
print(f'Seconds since epoch {time.time()}.')

# convert seconds epoch to string current time
print(time.ctime(time.time()))

# halt excecution for x seconds
time.sleep(0.01)

# returns boolean if daylight savings time is observed
print(time.daylight)

# convert time string to time format
# month and days start at 1
print(time.strptime("29 Jul 2020", "%d %b %Y"))

# convert a tuple represented by gmtime() or localtime() to a string
print(time.asctime(time.gmtime()))
print(time.asctime(time.localtime()))

# object with named tuple interface returned by gmtime(), localtime() and strptime()
# can be accessed by index and attributename
print(time.struct_time(time.gmtime()))

# takes number of seconds passed since epoch end returns a structured time object
print(time.localtime(time.time()))

# takes number of seconds passed since epoch end returns a structured time object if None is passed time() is used
print(time.gmtime(time.time()))

# takes struct_time object(or tuple containing 9 elements) as argument and returns seconds passed since epoch
print(time.mktime(time.gmtime()))

# takes struct_time object(or tuple containing 9 elements) as argument and returns string value of object
print(time.asctime(time.gmtime()))

# takes struct_time object(or tuple containing 9 elements) as argument and returns preformated string value of object
print(time.strftime("%m/%d/%Y, %H:%M:%S", time.gmtime()))

# takes string and returns struct_time object
print(time.strptime("21 June, 2018", "%d %B, %Y"))