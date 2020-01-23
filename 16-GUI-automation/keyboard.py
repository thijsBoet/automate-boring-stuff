import pyautogui

# give focus to text editor
pyautogui.click(100, 100)

# type
pyautogui.typewrite('Hello World')

# add interval per character
pyautogui.typewrite('Hello World', interval=0.2)
