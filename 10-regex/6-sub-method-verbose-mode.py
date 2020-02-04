# ---------------------------- Sub method and Verbose mode -------------------------------
import re

nameRegex = re.compile(r'Agent \w+')
print(nameRegex.findall('Agent Scully gave the secret documents to Agent Alice.'))

# Use sub method for find and replace action
print(nameRegex.sub('REDACTED', 'Agent Scully gave the secret documents to Agent Alice.'))

# Use groups to partially replace strings
nameRegex = re.compile(r'Agent (\w)\w*')
# Use \1 for first group, \2 for second group etc
print(nameRegex.sub(r'Agent \1*****', 'Agent Scully gave the secret documents to Agent Alice.'))

# with re.VERBOSE flag we can ignore spaces, returns, comments and tabs
phoneRegex = re.compile(r'''
\d\d\d      # area code
-           # first dash
\d\d\d      # first 3 digits
-           # second dash
\d\d\d\d    # last 4 digits''', re.VERBOSE)

# with the | or operator we can pass multiple flags in the compile method
nameRegex = re.compile(r'Agent \w+', re.I | re.DOTALL | re.VERBOSE))