# Convert the dictionary values to strings.


def stringifyNumbers(data):
    pass


if __name__ == "__main__":

    obj = {
        "num": 1,
        "test": [],
        "data": {"val": 4, "info": {"isRight": True, "random": 66}},
    }

    print(stringifyNumbers(obj))

    # Output:
    # {
    #     "num": "1",
    #     "test": [],
    #     "data": {"val": "4", "info": {"isRight": True, "random": "66"}},
    # }
