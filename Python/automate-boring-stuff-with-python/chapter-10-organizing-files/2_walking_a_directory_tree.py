# Walking a directory tree

import os


# os.walk() returns a generator that yields a tuple for each directory
for folderName, sub_folders, filenames in os.walk(
    r"learning-programming\Python\automate-boring-stuff-with-python\chapter-10-organizing-files"
):

    print("The current folder is " + folderName)
    
    for subfolder in sub_folders:
        print("SUBFOLDER OF " + folderName + ": " + subfolder)
    for filename in filenames:
        print("FILE INSIDE " + folderName + ": " + filename)
        print("")
