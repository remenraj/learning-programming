#! /usr/bin/env python3

# recursive function to collect strings
def collectStrings(Obj):
    # base case
    collected = []
    
    # loop through the keys in the dictionary
    for item in Obj:
        # if the item is a dictionary, call the function again
        if type(Obj[item]) is dict:
            collected += collectStrings(Obj[item])
        # if the item is a string, add it to the list
        else:
            collected.append(Obj[item])
    # return the list
    return collected


# test cases
if __name__ == "__main__":
    obj = {
        "stuff": "foo",
        "data": {
            "val": {
                "thing": {
                    "info": "bar",
                    "moreInfo": {"evenMoreInfo": {"weMadeIt": "baz"}},
                }
            }
        },
    }

    print(collectStrings(obj))  # ['foo', 'bar', 'baz'])
