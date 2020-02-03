# ---------------------------- Character Classes -------------------------------------------------------------------------
import re


# Char class        matches
# ------------------------------------------------------------------------------------------------------------------------
# \d                Any numeric digit from 0 to 9.
# \D                Any character that is not a numeric digit from 0 to 9.
# \w                Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)
# \W                Any character that is not a letter, numeric digit, or the underscore character.
# \s                Any space, tab, or newline character. (Think of this as matching “space” characters.)
# \S                Any character that is not a space, tab, or newline.
# a-zA-Z            Any character between a and z or A and Z

lyrics = '''On the first day of Christmas
my true love sent to me:
A Partridge in a Pear Tree

On the second day of Christmas
my true love sent to me:
2 Turtle Doves
and a Partridge in a Pear Tree


On the third day of Christmas
my true love sent to me:
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree

On the fourth day of Christmas
my true love sent to me:
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree

On the fifth day of Christmas
my true love sent to me:
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree

On the sixth day of Christmas
my true love sent to me:
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree


On the seventh day of Christmas
my true love sent to me:
7 Swans a Swimming
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree

On the eighth day of Christmas
my true love sent to me:
8 Maids a Milking
7 Swans a Swimming
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree

On the ninth day of Christmas
my true love sent to me:
9 Ladies Dancing
8 Maids a Milking
7 Swans a Swimming
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree

On the tenth day of Christmas
my true love sent to me:
10 Lords a Leaping
9 Ladies Dancing
8 Maids a Milking
7 Swans a Swimming
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree

On the eleventh day of Christmas
my true love sent to me:
11 Pipers Piping
10 Lords a Leaping
9 Ladies Dancing
8 Maids a Milking
7 Swans a Swimming
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree

On the twelfth day of Christmas
my true love sent to me:
12 Drummers Drumming
11 Pipers Piping
10 Lords a Leaping
9 Ladies Dancing
8 Maids a Milking
7 Swans a Swimming
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and 1 Partridge in a Pear Tree'''

# find one or more numbers followed by a space and one or more letters
xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(lyrics))

# use [wanted character] to create your own char classes
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('Robocop eats baby food'))

# use {times} to match exact repetitions of the regex
doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')
print(doubleVowelRegex.findall('Robocop eats baby food'))

# use ^ to create negative character class => match everything but these characters
NegVowelRegex = re.compile(r'[^aeiouAEIOU]')
print(NegVowelRegex.findall('Robocop eats baby food'))

# findall vs search method
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
resume = '''JANE SOMEBODY
123 Anywhere Street, City, State
555-000-0000
janesomebody@emailprovider.com

PROFILE

State the type of job you are seeking and highlight several of your most important, impressive and marketable skills.

SUMMARY OF SKILLS

- Include your most marketable skills and accomplishments here.

WORK EXPERIENCE

Administrative Assistant, XYZ Company, City, State, 2000 to 2006
- Continue to use verbs and nouns to describe job duties and accomplishments that are most relevant to the work you are currently seeking and target important keywords.

EDUCATION

Administrative Assistant Certificate, Any College, City, State 555-451-2315'''

# search finds first match only as a match object
print(phoneRegex.search(resume))

# findall returns all matches as a list
print(phoneRegex.findall(resume))

# findall returns a list of tuples when regex contains groups
phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
print(phoneRegex.findall(resume))

# can return a full number (with dashes) as first tuple by nesting it in another group
phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
print(phoneRegex.findall(resume))
  