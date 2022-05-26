# Create a Mad Libs program that reads in text files and lets the user add their own text anywhere the word
# ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.
# Automate the boring stuff with python, chapter 9, project 230

import pyinputplus as pyip


mad_libs_dir = r"learning-programming\Python\automate-boring-stuff-with-python\chapter-9-reading-and-writing-files\projects"

adjective = pyip.inputStr("Enter an adjective: ")
noun1 = pyip.inputStr("Enter a noun: ")
verb = pyip.inputStr("Enter a verb: ")
noun2 = pyip.inputStr("Enter a noun: ")

with open(f"{mad_libs_dir}\mad_libs.txt", "a") as mad_libs_file:
    print(
        f"The {adjective} panda walked to the {noun1} and then {verb}. A nearby {noun2} was unaffected by these events."
    )
    mad_libs_file.write(
        f"The {adjective} panda walked to the {noun1} and then {verb}. A nearby {noun2} was unaffected by these events.\n"
    )
