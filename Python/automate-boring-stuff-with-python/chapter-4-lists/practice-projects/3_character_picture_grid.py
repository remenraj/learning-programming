# chapter 4: Lists
# Practice Project: Character Picture Grid, page number: 108

"""
Program that prints the image

..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....

from the grid below
"""

grid = [
    [".", ".", ".", ".", ".", "."],
    [".", "O", "O", ".", ".", "."],
    ["O", "O", "O", "O", ".", "."],
    ["O", "O", "O", "O", "O", "."],
    [".", "O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O", "."],
    ["O", "O", "O", "O", ".", "."],
    [".", "O", "O", ".", ".", "."],
    [".", ".", ".", ".", ".", "."],
]


def picture_grid():
    """Function that converts the grid into a picture"""

    m = len(grid)
    n = len(grid[0])

    for i in range(n):

        for j in range(m):

            print(grid[j][i], end="")

        print()


if __name__ == "__main__":
    picture_grid()
