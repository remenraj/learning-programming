# Chapter 5: Dictionaries and Structuring, Page Number: 127
# Program to solve the challenge in chapter 5 of the book

import pprint


def display_inventory(inventory):
    """Displays the player inventory"""

    # formatting the inventory dictionary
    pprint.pformat(inventory)

    print("Inventory:")

    total_items = 0

    # printing the inventory
    for item in inventory:
        print(f"{inventory[item]} {item}")
        total_items += inventory[item]

    print(f"Total number of items: {total_items}")


def add_to_inventory(inventory, added_items):
    """Adds items to the inventory"""
    for item in added_items:
        if item in inventory.keys():
            inventory[item] += 1

        # if item is not in the inventory, add it as default
        inventory.setdefault(item, 1)

    return inventory


if __name__ == "__main__":

    player_inventory = {
        "arrow": 12,
        "gold coin": 42,
        "rope": 1,
        "torch": 6,
        "dagger": 1,
    }
    # Q1
    dragon_loot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
    display_inventory(inventory=player_inventory)

    # Q2
    player_inventory = {"gold coin": 42, "rope": 1}
    updated_inventory = add_to_inventory(
        inventory=player_inventory, added_items=dragon_loot
    )
    display_inventory(inventory=player_inventory)
