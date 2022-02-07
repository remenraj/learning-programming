# coffee machine program
from data import MENU, resources
from art import hot_beverage

# total income made by selling beverages
INCOME = 0


def prompt():
    """Prompts the user for espresso/latte/cappuccino and returns the choice"""

    # checking for valid input
    valid_input = False
    while not valid_input:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if (
            choice == "espresso"
            or choice == "latte"
            or choice == "cappuccino"
            or choice == "off"
            or choice == "report"
        ):
            valid_input = True
            return choice
        else:
            valid_input = False
            print("Invalid input. Try again.")


def check_resources(beverage):
    """Takes an input beverage and checks if there is sufficient resources and returns True/False"""

    for item in beverage["ingredients"]:
        if beverage["ingredients"][item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False

    return True


def calc():
    """Asks the user to insert coins, calculates total and returns it"""

    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    total_coin_value_inserted = (
        0.25 * quarters + 0.10 * dimes + 0.05 * nickels + 0.01 * pennies
    )

    return total_coin_value_inserted


def is_transaction_success(total_value, beverage_cost):
    """Returns true if successful transaction"""

    if total_value >= beverage_cost:

        # checking for change to be given
        if total_value > beverage_cost:
            change = round(total_value - beverage_cost, 2)
            print(f"Here is ${change} in change.")

        # adding income made
        global INCOME
        INCOME += beverage_cost
        return True

    else:

        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(beverage, choice):
    """Updates the resources after making beverage"""

    global resources

    for item in beverage["ingredients"]:
        resources[item] -= beverage["ingredients"][item]

    print(f"Here is your {choice}. Enjoy!")
    print(hot_beverage)


def coffee_machine():

    # running the coffee machine as long as it is not turned off
    is_turned_off = False
    while not is_turned_off:

        # asking the user for beverage
        user_input = prompt()

        # checking if the user wants to turn off the coffee machine
        if user_input == "off":
            is_turned_off = True

        # checking if the user wants to view the report
        elif user_input == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${INCOME}")

        else:
            chosen_beverage = MENU[user_input]

            # checking for sufficient resources
            if check_resources(beverage=chosen_beverage):

                # printing cost of chosen beverage
                print(f"Cost of {user_input} = ${chosen_beverage['cost']}")

                # prompting user for coins and calculating the total value of coins inserted
                total_inserted = calc()

                # checking for successful transaction
                if is_transaction_success(
                    total_value=total_inserted, beverage_cost=chosen_beverage["cost"]
                ):

                    make_coffee(beverage=chosen_beverage, choice=user_input)


coffee_machine()
