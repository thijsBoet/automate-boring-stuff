# ---------------------------- Dot Star and Caret Dollar -------------------------------
import re

# start with a catet ^... to match with strings that start with that sequence of characters
beginsWithHelloRegex = re.compile(r'^Hello')
print(beginsWithHelloRegex.findall('Hello to all.'))

# end with a dollar $ to match with strings that end with that sequence of characters
endsWithWorldRegex = re.compile(r'World!$')
print(endsWithWorldRegex.findall('Hello World!'))

# can be combined to check entire text from beginning to end
allDigitRegex =  re.compile(r'^\d*$')
print(allDigitRegex.findall('1234567890'))

# use .*** for any character that can be placed on the dot
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

# use {min, max} characters in front the dot
atRegex = re.compile(r'.{1,2}at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

# use .* as a greedy wildcard
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall('First Name: Matthijs Last Name: Boet'))

# use .*? for non greedy wildcard
nongreedy = re.compile(r'<(.*?)>')
print(nongreedy.findall('<To serve humans> for dinner.>'))

# wildcard .* only look on first line not on consequent new lines
dotStar = re.compile(r'.*')
print(dotStar.search('Serve the public trust.\nProtect the innocent.\nUphold the law.'))

# can be bypassed with re.DOTALL flag
dotStar = re.compile(r'.*', re.DOTALL)
print(dotStar.search('Serve the public trust.\nProtect the innocent.\nUphold the law.'))

# can us re.IGNORECASE or re.I flag to ignore case
vowelRegex = re.compile(r'[aeiou]', re.I)
print(vowelRegex.findall('Al, ehy does your programming book talk about robocop so much.'))