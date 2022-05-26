# Copying and moving files and folders
# os.unlink() will delete a file
# os.rmdir() will delete a folder(but the folder must be empty)
# shutil.rmtree() will delete a folder and all its contents
# Deleting can be dangerous, so run a dry run first, that is without actually deleting anything.
# send2trash.send2trash() will send a file or folder to the recycling bin

import shutil, os, send2trash


#### Copy, move, and rename files and folders ####

# shutil module provides high-level file operations like copy and move.

# to copy a file or folder, use the copy() method:
# shutil.copy(source directory, destination directory)

# to move a file or folder, use the move() method:
# shutil.move(source directory, destination directory)

# to copy/move a file and rename it:
# shutil.copy("src-dir/file.txt", "dest-dir/new_name.txt")
# shutil.move("dir/file.txt", "dir/new_name.txt")   # this will rename the file


###### Deleting files and folders ########

# os.unlink(path="src-dir/file.txt")  # deletes a single file

# os.rmdir(path="dir")  # removes an empty directory

# to remove a file or folder, use the rmtree() method:
# this permanently deletes a directory and all of its contents, it'll not be send to the trash
# shutil.rmtree(path="src-dir")  # removes a directory and all its contents


##### send2trash module: send files and folders to the trash instead of permanently deleting it ######

# send2trash.send2trash(paths="src-dir/file.txt") # send a file to the trash