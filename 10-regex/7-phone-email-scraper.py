#! python3
# ---------------------------- Phone and email scraper -------------------------------
import re, pyperclip

# Create regex for phone numbers

phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))?# area code (optional)
(\s|-)?                 # first separator
\d\d\d                  # first 3 digits
-                       # separator
\d\d\d\d                # last 4 digits
(((ext(\.)?\s)|x)       # extention word-part (optional)
(\d{2,5}))?             # extention number-part (optional)
)
''', re.VERBOSE)

# Create regex for email addresses

emailRegex = re.compile(r'''
# some._%+-12@some.+_12.com

[a-zA-Z0-9._%+-]+       # name part
@                       # @ symbol
[a-zA-Z0-9._%+-]+       # domain name
\.[a-zA-Z{2,4}]        # domain extention

''', re.VERBOSE)

# Get text off the clipboard
text = pyperclip.paste()

# Extract the email/phone from the text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# Copy extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)

print(f'Copied {results} to clipboard.')