#! python3
# Adds Wikipedia bullet points to the start of each line of text on the clipboard.

import pyperclip


# reading from clipboard
# text = pyperclip.paste()

text = """Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars"""

# converting the text into list of lines
line = text.split("\n")

# adding * to the first line of every
line[0] = "* " + line[0]
text = "\n* ".join(line)

# # another method for adding *
# for i in range(len(line)):
#     line[i] = "* " + line[i]
# text = "\n".join(line)


print(text)

# copying text to clipboard
pyperclip.copy(text)
