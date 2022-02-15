# Password Generator Project
import random

# list of alphabets
letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

# list of numbers
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# list of symbols
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

# welcome message
print("Welcome to the PyPassword Generator!")
# prompting the user for various input
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

""" Easy level code. Order not randomized:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# initializing the password
password = ""

# adding random letters to the password
for n in range(0, nr_letters):
    password += random.choice(letters)

# adding random symbols to the password
for n in range(0, nr_symbols):
    password += random.choice(symbols)

# adding random numbers to the password
for n in range(0, nr_numbers):
    password += random.choice(numbers)

#printing the password
print(f"Your password is {password}")
"""

# Hard Level - Order of characters randomized:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# initializing the password list
password_list = []

# adding random letters to the password
for n in range(0, nr_letters):
    password_list.append(random.choice(letters))

# adding random symbols to the password
for n in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

# adding random numbers to the password
for n in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

# shuffling the list
random.shuffle(password_list)

# initializing password string
password = ""
for char in password_list:
    password += char


# printing the password
print(f"Your password (hard level) is {password}")
