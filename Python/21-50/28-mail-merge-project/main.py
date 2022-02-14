#! /usr/bin/env python3
# Create a letter using starting_letter.txt for each name in invited_names.txt
# Save the letters in the folder "ReadyToSend".
# The letter should be saved in the format of "letter_for_[name].txt"

# file directories
NAMES_DIRECTORY = r"learning-programming\Python\21-50\28-mail-merge-project\Input\Names\invited_names.txt"
STARTING_LETTER_DIR = r"learning-programming\Python\21-50\28-mail-merge-project\Input\Letters\starting_letter.txt"
READY_TO_SEND_DIR = (
    r"learning-programming\Python\21-50\28-mail-merge-project\Output\ReadyToSend"
)


def mail_merge():
    """Create a letter using starting_letter.txt for each name in invited_names.txt"""
    try:
        # opening files and reading data
        with open(NAMES_DIRECTORY) as name_file:
            name_list = name_file.readlines()
    except:
        print("Error: Could not open file:", NAMES_DIRECTORY)

    try:
        # reading the starting letter and saving it in a variable
        with open(STARTING_LETTER_DIR) as starting_letter:
            starting_letter = starting_letter.read()
    except:
        print("Error: Could not open file:", STARTING_LETTER_DIR)

    # creating a list of letters
    for name in name_list:
        # removing the new line character from the name
        stripped_name = name.strip()
        # creating the file name
        file_name = "letter_for_" + stripped_name + ".txt"
        # replacing the name in the starting letter
        edited_letter = starting_letter.replace("[name]", stripped_name)
        # writing the letter to the file
        with open(f"{READY_TO_SEND_DIR}\\{file_name}", "w") as new_letter:
            new_letter.write(edited_letter)


# calling the main function
if __name__ == "__main__":
    mail_merge()
