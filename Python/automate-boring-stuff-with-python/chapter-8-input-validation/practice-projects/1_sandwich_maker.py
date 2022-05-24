# Sandwich maker, Automate the boring stuff with python, chapter 8, page number: 198

import pyinputplus as pyip
import time


def sandwich_maker() -> None:
    """Make a sandwich"""

    bread_type = pyip.inputMenu(
        ["Wheat", "White", "Rye"], numbered=True, prompt="What kind of bread?\n"
    )
    print(f"You chose {bread_type} bread.")

    protein_type = pyip.inputMenu(
        ["Chicken", "Turkey", "Ham", "Tuna", "Salami"],
        numbered=True,
        prompt="What kind of protein?\n",
    )
    print(f"You chose {protein_type}.")

    if pyip.inputYesNo("Do you want cheese? yes/no:") == "yes":
        cheese_type = pyip.inputMenu(
            ["Cheddar", "Swiss", "American"], "What kind of cheese?\n", numbered=True
        )
        print(f"Your cheese is {cheese_type}")

    if (
        pyip.inputYesNo("Do you want mayo, mustard, lettuce, or tomato? yes/no: ")
        == "yes"
    ):
        addon_type = pyip.inputMenu(
            ["Mayo", "Mustard", "Lettuce", "Tomato"], "Choose One:\n", numbered=True
        )
        print(f"You chose: {cheese_type}")

    number_of_sandwiches = pyip.inputInt(
        prompt="How many sandwiches would you like to make?: ", min=1
    )

    time.sleep(1)
    print("Your sandwich is ready!")


if __name__ == "__main__":
    sandwich_maker()
