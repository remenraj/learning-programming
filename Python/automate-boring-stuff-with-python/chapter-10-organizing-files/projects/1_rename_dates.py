# Renames filenames with American MM-DD-YYYY date format to European DD-MM-YYYY

import shutil, os, re


# Create a regex that matches files with the American date format.
date_pattern = re.compile(r"""
                          ^(.*?)        # all text before the date
                        ((0|1)?\d)-     # one or two digits for the month
                        ((0|1|2|3)?\d)- # one or two digits for the day
                        ((19|20)\d\d)   # four digits for the year
                        (.*?)$          # all text after the date
                        """, re.VERBOSE)


# Loop over the files in the working directory.
for american_filename in os.listdir('.'):
    mo = date_pattern.search(american_filename)
    
    # Skip files without a date.
    if mo == None:
        continue
    
    # Get the different parts of the filename.
    before_part = mo.group(1)
    month_part = mo.group(2)
    day_part = mo.group(4)
    year_part = mo.group(6)
    after_part = mo.group(8)
    
    # Form the European-style filename.
    euro_filename = before_part + day_part + '-' + month_part + '-' + year_part + after_part
    
    # Get the full, absolute file paths.
    abs_working_dir = os.path.abspath('.')
    american_filename = os.path.join(abs_working_dir, american_filename)
    euro_filename = os.path.join(abs_working_dir, euro_filename)
    
    # Rename the files.
    print(f'Renaming "{american_filename}" to "{euro_filename}"...')
    #shutil.move(amerFilename, euroFilename) # uncomment after testing