# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, 
# write a method to rotate the image by 90 degrees.

# input matrix:
# 1 2 3
# 4 5 6
# 7 8 9

# output matrix:
# 7 4 1
# 8 5 2
# 9 6 3

# # algorithm
# for i = 0 to n:
#     temp = top_left[i]
#     top_left[i] = bottom_left[i]
#     bottom_left[i] = bottom_right[i]
#     bottom_right[i] = top_right[i]
#     top_right[i] = temp

import numpy as np


def rotate_matrix(matrix: np.array) -> np.array:
    """Rotates the matrix by 90 degrees"""
    
    n = len(matrix)
    
    for layer in range(n // 2):
        
        first = layer 
        last = n - layer - 1
        
        for i in range(first, last):
            # save top left element
            top = matrix[layer][i]

            # bottom left -> top left
            matrix[layer][i] = matrix[-i - 1][layer]

            # bottom right -> bottom left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

            # top right -> bottom right
            matrix[-layer - 1][-i - 1] = matrix[i][- layer - 1]

            # top left -> top right
            matrix[i][- layer - 1] = top
    
    
    # # another method
    # # transpose the matrix
    # matrix = matrix.transpose()

    # # flip the matrix
    # matrix = np.flip(matrix, 1)

    return matrix

    # # another method
    # n = len(matrix)
    # temp = np.copy(matrix)
    
    # for i in range(n):
    #     for j in range(n):
    #         temp[i][j] = matrix[(n-1) - j][i]

    # return temp


def main() -> None:
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(matrix)
    print(rotate_matrix(matrix))


if __name__ == "__main__":
    main()