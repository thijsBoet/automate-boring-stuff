import os

# os.path.join returns right file path for current OS
print(os.path.join('User', 'David', 'Documents', 'todo.txt'))

# get C-W-D Current Working Directory
print(os.getcwd())

# change Current Working Directory
os.chdir('D:\\python\\automate-boring-stuff')

# returns absolute file path of given file
print(os.path.abspath('files.py'))

# checks if the file path is absolute
print(os.path.isabs('..\\..\\files.py'))

# returns a relative file path from the second argument to the first argument
print(os.path.relpath('D:\\python\\automate-boring-stuff\\files.py', 'D:\\python\\python-dev-2020'))

# returns path of current directory
print(os.path.dirname('D:\\python\\automate-boring-stuff\\files.py'))

# returns name of the file in current file path
print(os.path.basename('D:\\python\\automate-boring-stuff\\files.py'))

# checks for existence of file path
print(os.path.exists('D:\\python\\python-dev-2020\\web-scraper'))

# checks for a folder path
print(os.path.isdir('D:\\python\\python-dev-2020\\web-scraper'))

# checks for a file path
print(os.path.isfile('D:\\python\\python-dev-2020\\web-scraper'))

# returns size in bytes as an integer
print(os.path.getsize('D:\\python\\automate-boring-stuff\\files.py'))

# returns list of files in given directory
print(os.listdir('D:\\python\\automate-boring-stuff'))

totalSize = 0

for filename in os.listdir('D:\\python\\automate-boring-stuff'):
    if not os.path.isfile(os.path.join('D:\\python\\automate-boring-stuff', filename)):
        continue
    totalSize += os.path.getsize(os.path.join('D:\\python\\automate-boring-stuff', filename))
print(totalSize)

# os.makedirs('C:\\delicious\\walnut\\waffles') => create folders