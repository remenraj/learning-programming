# The open() function will return a file object which has reading and writing –related methods.
# Pass ‘r' (or nothing) to open() to open the file in read mode. Pass ‘w' for write mode. Pass ‘a' for append mode.
# Opening a nonexistent filename in write or append mode will create that file.
# Call read() or write() to read the contents of a file or write a string to a file.
# Call readlines() to return a list of strings of the file's content.
# Call close() when you are done with the file.
# The shelve module can store Python values in a binary file.
# The shelve.open() function returns a dictionary-like shelf value.

import shelve


# open(): open a file
hello_file = open("C:\\test\\hello.txt")  # open plain text file in read mode
print(hello_file.read())  # read the contents of the file
print(hello_file.readlines())  # read the contents of the file as a list of strings
hello_file.close()  # close the file

# open a files in write mode
hello_file = open("C:\\test\\hello2.txt", "w")  # open plain text file in write mode
hello_file.write("Hello\nEarth")  # write a string to the file
hello_file.close()  # close the file

# append mode (add to the end of the file)
hello_file = open("C:\\test\\hello2.txt", "a")  # open plain text file in append mode
hello_file.write("\nHello\nEarth")  # write a string to the file
hello_file.close()  # close the file

# shelve module: store Python values in a binary file
# can be used to store list, dictionary, and other Python objects
shelf_file = shelve.open("mydata")  # open a shelve file
shelf_file["cats"] = ["Zophie", "Pooka", "Simon"]  # store a list in the shelf
shelf_file.close()  # close the shelf

# retrieving the data
shelf_file = shelve.open("mydata")
print(shelf_file["cats"])  # retrieve a list from the shelf

# it also accepts key value pairs
print(list(shelf_file.keys()))  # list the keys in the shelf
print(list(shelf_file.values()))  # list the values in the shelf
shelf_file.close()
