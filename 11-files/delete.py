import os

# delete single file
# os.unlink('bacon.txt')

# delete empty folder
# os.rmdir('../tmp/backup')

import shutil
# delete folder and everything in it
# shutil.rmtree('../tmp/backup')

for filename in os.listdir():
    if filename.endswith('txt'):
        os.unlink(filename)
        print(filename)

# all deletions are permanent 
# use 3rd party import send2trash for safety
# import send2trash
# send2trash.send2trash('filename')