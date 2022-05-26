# Regex search, automate the boring stuff with Python, page number: 230
# A program that opens all .txt files in a folder and searches for any line that matches a user-supplied regular expression. 
# The results should be printed to the screen.

from ast import Str
import os, re


def txt_search(dir: str, pattern: str) -> None:
    
    for file_name in os.listdir(dir):
        if file_name.endswith(".txt"):
            file = open(os.path.join(dir, file_name), "r")
            for line in file:
                if re.search(pattern, line):
                    print(line)
            file.close()


if __name__ == "__main__":
    
    # directory to search txt files
    src_dir = r"learning-programming\Python\automate-boring-stuff-with-python\chapter-9-reading-and-writing-files\projects\quiz-data"

    # regex pattern to search
    regex = r"\d{3}-\d{3}-\d{4}"
    
    txt_search(dir=src_dir)