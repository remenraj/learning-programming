# compressing files with the zipfile module

import zipfile, os
from pathlib import Path


# home directory
p = Path.home()
print(p)

# current working directory
p = Path.cwd()
print(p)


# # reading zip files
example_zip = zipfile.ZipFile(p / r'learning-programming\Python\automate-boring-stuff-with-python\chapter-10-organizing-files\example.zip')

spam_info = example_zip.getinfo('spam.txt') # get info about the file
print(spam_info.file_size)  # get the size of the file
print(spam_info.compress_size)  # get the compressed size of the file

# example_zip.extractall()    # extracting zip file
# example_zip.extract('spam.txt')  # extracting a specific file
# example_zip.extract('spam.txt', 'C:\\some\\new\\folders')   # extracting a specific file to a new folder
example_zip.close()


# # creating a new zip file
# new_zip = zipfile.ZipFile('new.zip', 'w')
# new_zip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
# new_zip.close()