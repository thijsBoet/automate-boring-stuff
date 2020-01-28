#! python3
# stopwatch.py - a simple stopwatch program

import time

# Display program instructions
print('Press ENTER to begin. Afterward, press ENTER to start stopwatch.\nPress Ctrl-C to quit.')
input()             # press enter to begin
print('Started')

startTime = time.time()
lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time()  # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.\n')

for i in range(5):
    print('Tick')
    time.sleep(1)
    print('Tock')
    time.sleep(1)