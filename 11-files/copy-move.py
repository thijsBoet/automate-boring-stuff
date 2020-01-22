import shutil

# copy file to 2nd argument
shutil.copy('D:\\python\\automate-boring-stuff\\11-files\\hello.txt', 'D:\\python\\automate-boring-stuff\\tmp')

# copy file and rename to 2nd arguments filename
shutil.copy('D:\\python\\automate-boring-stuff\\11-files\\hello.txt', 'D:\\python\\automate-boring-stuff\\tmp\\renamed.txt')

# copy entire folder
shutil.copytree('D:\\python\\automate-boring-stuff\\11-files', 'D:\\python\\automate-boring-stuff\\tmp\\backup')

# move
# shutil.move('hello.txt', 'hello.txt')

# rename
# shutil.move('hello.txt', 'hello_new_name.txt')