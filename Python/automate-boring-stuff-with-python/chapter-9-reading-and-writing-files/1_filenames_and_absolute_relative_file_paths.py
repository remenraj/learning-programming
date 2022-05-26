# Files have a name and a path.
# The root folder is the lowest folder.
# In a file path, the folders and filename are separated by backslashes on Windows and forward slashes on Linux and Mac.
# Use the os.path.join() function to combine folders with the correct slash.
# The current working directory is the folder that any relative paths are relative to.
# os.getcwd() will return the current working directory.
# os.chdir() will change the current working directory.
# Absolute paths begin with the root folder, relative paths do not.
# The . folder represents "this folder", the .. folder represents "the parent folder".
# os.path.abspath() returns an absolute path form of the path passed to it.
# os.path.relpath() returns the relative path between two paths passed to it.
# os.makedirs() can make folders.
# os.path.getsize() returns a file's size.
# os.listdir() returns a list of strings of filenames.
# os.path.exists() returns True if the filename passed to it exists.
# os.path.isfile() and os.path.isdir() return True if they were passed a filename or file path.

import os


# os.path.join(): Combines folders and filename with the correct slash.
print(os.path.join("usr", "bin", "spam"))
file_path = os.path.join(os.getcwd(), "test.txt")
print(file_path)


# current working directory
print(os.getcwd())


# change current working directory
os.chdir("C:\\Users\\Cylon\\OneDrive")  # changing the current working directory to c:\

# Absolute and Relative Paths
# example of absolute file path: c:\test.txt
# example of relative file path: test.txt

# .: current folder
# ..: parent folder
print(os.path.abspath("."))  # C:\Users\Cylon\OneDrive
print(os.path.abspath(".."))  # C:\Users\Cylon

print(os.path.abspath("test.txt"))  # absolute path # C:\Users\Cylon\OneDrive\test.txt
print(os.path.relpath("test.txt"))  # relative path # test.txt

# check if path is absolute:
print(os.path.isabs("test.txt"))  # False
print(os.path.isabs("C:\\Users\\Cylon"))  # True

# retrieve path components:
print(
    os.path.split("C:\\Users\\Cylon\\OneDrive\\test.txt")
)  # ('C:\\Users\\Cylon\\OneDrive', 'test.txt')

# retrieve directory name:
print(
    os.path.dirname("C:\\Users\\Cylon\\OneDrive\\test.txt")
)  # C:\Users\Cylon\OneDrive
# retrieve file name/last folder name:
print(os.path.basename("C:\\Users\\Cylon\\OneDrive\\test.txt"))  # test.txt


# check if path exists:
print(os.path.exists("C:\\Users\\Cylon\\OneDrive\\test.txt"))  # False

# check if it is a folder:
print(os.path.isdir("C:\\Users\\Cylon\\OneDrive"))  # True

# check if it is a file:
print(os.path.isfile("C:\\windows\\system32\\calc.exe"))  # True

# get the size of a file:
print(os.path.getsize("C:\\windows\\system32\\calc.exe"))

# get a list of folder/files inside a directory:
print(os.listdir("C:\\Users\\Cylon\\OneDrive"))

# make a folder:
# os.makedirs("C:\\Users\\Cylon\\OneDrive\\test")