# -----------------------------Repetition Patterns--------------------------------
import re

# (...)? this group of characters can appear zero or one times
batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The adventures of Batman')
print(mo.group())

mo = batRegex.search('The adventures of Batwoman')
print(mo.group())

# optional area code
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phonenumber is 555-4561')
print(mo.group())

# use * to match zero or more times (just like ?, but allows more than one match)
batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The adventures of Batwowowowowoman')
print(mo.group())

# use + to match one or more times (just like *, but must match at least once)
batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search('The adventures of Batwowowowowoman')
print(mo.group())

# use {times} to match exact repetitions
haRegex = re.compile(r'(Ha){3}')
mo = haRegex.search('He said HaHaHa')
print(mo.group())

# use {minimum, maximum} to match range of repetitions
naRegex = re.compile(r'(Na){1,5}')
mo = naRegex.search('She said NaNaNaNaNa')
print(mo.group())

# still matches the first five maximum characters
# aka greedy matching => match the longest posible string
digitRegex = re.compile(r'(\d){3,5}')
mo = digitRegex.search('1234567890')
print(mo.group())

# to do a non greedy match append a '?' to the end expression
# a non greedy matches => the smallest possible string
digitRegex = re.compile(r'(\d){3,5}?')
mo = digitRegex.search('1234567890')
print(mo.group())