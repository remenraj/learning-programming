# program that calculates the total amount each person should pay

# asking and storing the total bill amount
bill_amount = float(input("Welcome to the tip calculator!\nWhat was the total bill? $"))

# percentage of tip to be applied to the bill
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))

# asking for the total number of people in the group
total_people = int(input("How many people to split the bill? "))

# calculating the total bill amount with tip
bill_with_tip = bill_amount * (1 + tip_percentage/100)

# calculating the amount to be paid by each person and rounding off to 2 decimal places
split_amount = "{:.2f}".format(bill_with_tip/total_people)

# printing the amount to be paid by each person
print(f"Each person should pay: ${split_amount}")