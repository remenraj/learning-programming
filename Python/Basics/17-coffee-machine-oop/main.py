## Coffee Machine using Object Oriented Programming
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def coffee_machine():
    """Coffee Machine code"""

    # object contains report, check for sufficient resources, make coffee(deducts the ingredients from resources)
    coffee_maker = CoffeeMaker()

    # object contains get_item(returns string of menu), find_drink(returns true if drink is found)
    menu = Menu()

    # object contains report(total income made)
    money_machine = MoneyMachine()

    # running the coffee machine until it is turned off
    is_turned_off = False
    while not is_turned_off:

        # asking the user for beverage
        user_choice = input(f"What would you like? {menu.get_items()}: ").lower()

        # checking if the user wants to turn off the coffee machine
        if user_choice == "off":
            is_turned_off = True

        # checking if the user wants to view the report
        elif user_choice == "report":
            coffee_maker.report()
            money_machine.report()

        else:
            beverage = menu.find_drink(user_choice)

            # checking for sufficient resources and successful transaction
            if coffee_maker.is_resource_sufficient(
                beverage
            ) and money_machine.make_payment(beverage.cost):

                # make coffee, deduct resources
                coffee_maker.make_coffee(beverage)


coffee_machine()
