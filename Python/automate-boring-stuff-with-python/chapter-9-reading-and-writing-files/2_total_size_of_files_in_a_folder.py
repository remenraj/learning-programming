# Program to calculate the total size of files inside a folder

import os

total_size = 0

for filename in os.listdir('C:\\Users\\Cylon\\OneDrive'):
    if os.path.isfile(os.path.join('C:\\Users\\Cylon\\OneDrive', filename)):    # check if it is a file
        total_size += os.path.getsize(os.path.join('C:\\Users\\Cylon\\OneDrive', filename))
        
print(total_size)