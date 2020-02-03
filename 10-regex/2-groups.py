# -----------------------------Groups--------------------------------
import re

# use () to create goups like area code and phonenumber
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# .search() returns a match object
matchObject = phoneNumRegex.search('My number is 415-555-4242')

# .group(1) returns the group one
print(matchObject.group(1))
# .group(2) returns the group two
print(matchObject.group(2))

# use \ (backslash) to escape characters => \(---\)
phoneNumRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
matchObject = phoneNumRegex.search('My number is (415) 555-5454')
# use .group() or .group(0) to return the entire matched string
print(matchObject.group())

# use | character as or operator in strings
batRegex = re.compile(r'Bat(man|mobile|copter|woman)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())

# return None if no matches are found
mo = batRegex.search('Batcycle lost a wheel')
print(mo == None)