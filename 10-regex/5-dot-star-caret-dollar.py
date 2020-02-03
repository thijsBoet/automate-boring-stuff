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