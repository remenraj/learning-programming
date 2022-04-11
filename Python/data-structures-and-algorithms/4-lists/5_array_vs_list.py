# Array vs List

# Similarities

# 1. Both data structures are mutable.
# 2. Bot can be indexed and iterated through.
# 3. They can be both sliced.


# Differences

# 1. Arrays are optimized for Arithmetic Operations
# 2. In lists you can use any data type, but in arrays you can only use same data types.

import numpy as np

# example for arithmetic operations
my_array = np.array([1, 2, 3, 4, 5, 6])
my_list = [1, 2, 3, 4, 5, 6]

print(my_array / 2)
# print(my_list/2)  # TypeError: unsupported operand type(s) for /: 'int' and 'int'
