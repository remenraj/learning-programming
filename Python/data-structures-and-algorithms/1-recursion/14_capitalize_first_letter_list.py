# Function to capitalize first letter of each word in a list

# recursive function
def capitalizeFirst(lst):
    # base case
    if len(lst) == 0:
        return []

    # recursive case
    return [lst[0][0].upper() + lst[0][1:]] + capitalizeFirst(lst[1:])
    # return [lst[0].capitalize()] + capitalizeFirst(lst[1:])


if __name__ == "__main__":
    print(capitalizeFirst(["car", "taco", "banana"]))  # ['Car','Taco','Banana']
