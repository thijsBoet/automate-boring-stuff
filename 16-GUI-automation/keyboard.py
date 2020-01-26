import pyautogui

# give focus to text editor
pyautogui.click(2600, 70)

# type
pyautogui.typewrite('Hello World ')

# add interval per character
pyautogui.typewrite('Hello World ', interval=0.01)

# can give it a list with cursor movements in it
pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'], interval=0.01)

# keyboard keywords in pygui
print(pyautogui.KEYBOARD_KEYS)

# alternative syntac => pyautogui.press('KEYWORD_KEY')

# keyboard shortcuts like ctrl C
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'x')

pyautogui.press('enter')
pyautogui.hotkey('ctrl', 'v')
