import pyautogui

# Image recognition is computational intensive (around a second per operation)
# Search material has to be pixel perfect representations of the search screenshot area

# take screenshot and save it parameter image .png file
pyautogui.screenshot('screenshot.png')

# locate x, y, width and height of paramenter image in screenshot
print(pyautogui.locateOnScreen('close.png'))

# locate x and y coordinates of parameter image and move to is center during half a second
pyautogui.moveTo(pyautogui.locateCenterOnScreen('close.png'), duration=0.5)