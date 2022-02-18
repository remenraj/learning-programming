#! /usr/bin/env python3
# Program to convert a string into NATO phonetic alphabet
import pandas


def nato_alphabet():
    """Converts a string into NATO Phonetic Alphabet"""
    # file directory
    try:
        NATO_PHONETIC_FILE_DIR = r"learning-programming\Python\21-50\33-NATO-phonetic-alphabet-converter"
    except FileNotFoundError:
        print(f"File not found: {NATO_PHONETIC_FILE_DIR}")

    # creating dataframe from csv file
    nato_df = pandas.read_csv(NATO_PHONETIC_FILE_DIR)

    # converting dataframe into dictionary
    nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

    # checking if the input is valid (string cannot contain symbols)
    valid_input = True
    while valid_input:
        user_input = input("Enter a word: ").upper()
        # converting word into NATO alphabet
        try:
            word_list = [nato_dict[letter] for letter in user_input]
        except KeyError:
            print("Sorry, only letters, numbers and spaces are allowed.")
        else:
            print(word_list)
            valid_input = False


# calling the main function
if __name__ == "__main__":
    nato_alphabet()
