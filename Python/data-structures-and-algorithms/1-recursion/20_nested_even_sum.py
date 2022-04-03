# Program to find the sum of all even numbers in a nested dictionary


# recursive method
def nestedEvenSum(obj):
    # base case
    sum = 0
    # loop through the keys in the dictionary
    for item in obj:
        # if the item is an even number, add it to the sum
        if type(obj[item]) is int and obj[item] % 2 == 0:
            sum += obj[item]
        
        # if the item is a dictionary, call the function again     
        if type(obj[item]) is dict:
            sum += nestedEvenSum(obj[item])
    # return the sum        
    return sum    

# test cases
if __name__ == "__main__":

    obj1 = {
    "outer": 2,
    "obj": {
        "inner": 2,
        "otherObj": {
        "superInner": 2,
        "notANumber": True,
        "alsoNotANumber": "yup"
        }
    }
    }

    obj2 = {
    "a": 2,
    "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
    "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
    "d": 1,
    "e": {"e": {"e": 2}, "ee": 'car'}
    }

    print(nestedEvenSum(obj1)) # 6
    print(nestedEvenSum(obj2)) # 10