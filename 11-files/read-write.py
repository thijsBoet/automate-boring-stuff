# returns file object in read mode
helloFile = open('D:\\python\\automate-boring-stuff\\11-files\\hello.txt')

# after read() is used must run open method again, therefore save read method to variable
content = helloFile.read()
helloFile.close()
print(content)

# readlines returns lines in list form
helloFile = open('D:\\python\\automate-boring-stuff\\11-files\\hello.txt')
lines = helloFile.readlines()
helloFile.close()
print(lines)

# cannot write to file in read mode, must use write mode (or append mode to append to end of file)
# second argument 'w' for write 'a' for append
# will overwrite existing file content or create new file if it does not exists
helloFile = open('D:\\python\\automate-boring-stuff\\11-files\\hello.txt', 'w')
helloFile.write('Hello World!\nHow are you?')

baconFile = open('bacon.txt', 'w')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()

baconFile = open('bacon.txt', 'a')
baconFile.write('\nBacon is delicious.')
baconFile.close()

baconFile = open('bacon.txt')
baconContent = baconFile.read()
print(baconContent)

import shelve
# use shelf module to save data-structures like dictionaries to files

shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['Assepoes', 'Parel', 'Simba', 'Yoda']
shelfFile.close()

shelfFile = shelve.open('mydata')
print(shelfFile['cats'])
shelfFile.close()