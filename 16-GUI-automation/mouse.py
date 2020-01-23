import pyautogui

# screensize
pyautogui.size()

# assign to width and height variables
width, height = pyautogui.size()

# mouse position
pyautogui.position()

# move to value x and value y
pyautogui.moveTo(10, 10)

# move slowly to value x and value y
pyautogui.moveTo(20, 20, duration = 0.1)

# move relative to current position
pyautogui.moveRel(200, 20)

# move slowly relative to current position
pyautogui.moveRel(440, 40, duration = 0.1)

# click on x and y value
pyautogui.click(1000, 500)

# double click on x and y value
pyautogui.doubleClick(1000, 500)

# right click on x and y value
pyautogui.rightClick(1000, 500)

# drag relative to
pyautogui.dragRel(100, 100, duration=0.1)

# display mouse position realtime
pyautogui.displayMousePosition()