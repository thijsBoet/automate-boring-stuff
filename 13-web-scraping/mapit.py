import webbrowser, sys, pyperclip

# check if commandline arguments are passed
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

# https://www.google.com/maps/place/{address}
webbrowser.open(f'https://www.google.com/maps/place/{address}')