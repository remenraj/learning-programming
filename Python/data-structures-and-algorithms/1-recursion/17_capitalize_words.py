# Program to capitalize words in a list using recursion

# recursive function
def capitalizeWords(word_list):

    assert (
        type(word_list) == list and type(word_list[0]) == str
    ), "It must be a list of strings"

    # base case
    capitalized = []
    if len(word_list) == 0:
        return capitalized

    # recursive case
    capitalized = word_list[0].upper()
    return [capitalized] + capitalizeWords(word_list[1:])


if __name__ == "__main__":

    words = ["i", "am", "learning", "recursion"]
    print(capitalizeWords(words))  # ['I', 'AM', 'LEARNING', 'RECURSION']
