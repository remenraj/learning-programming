# Example program for logging
# factorial of a number

import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

# logging.basicConfig(filename="myfilelog.txt", level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')   # writes the log messages into a file instead of the screen

# disable logging
# logging.disable(level=logging.CRITICAL)   # comment this line to enable logging

def factorial(n: int) -> int:
    """Returns factorial of a number"""

    logging.debug(f"Start of factorial {n}")

    total = 1
    
    for i in range(1, n + 1):
        total *= i
        logging.debug(f"i is {i}, total is {total}")
    
    logging.debug(f"Return value is {total}")
    return total


if __name__ == "__main__":
    logging.debug("Start of program")
    print(factorial(5))
    logging.debug("End of program")