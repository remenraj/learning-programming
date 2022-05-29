# Box Printing Assignment


def box_print(symbol: str, width: int, height: int) -> None:
    """Prints a box with the given symbol and width and height."""
    if len(symbol) != 1:
        raise Exception("Symbol must be a single character string.")
    if width <= 2 or height <= 2:
        raise Exception("Width and height must be greater than 2.")

    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (" " * (width - 2)) + symbol)

    print(symbol * width)


if __name__ == "__main__":
    box_print("*", 15, 5)
    box_print("O", 5, 5)
    # box_print("xx", 1, 1)
    # box_print("x", 4, 1)
