import os

for folderName, subfolders, filenames in os.walk('D:\\python\\automate-boring-stuff'):
    print(f'The folder is {folderName}')
    print(f'The subfolders in {folderName} are: {str(subfolders)}')
    print(f'The filenames in {folderName} are: {str(filenames)}')
    print()