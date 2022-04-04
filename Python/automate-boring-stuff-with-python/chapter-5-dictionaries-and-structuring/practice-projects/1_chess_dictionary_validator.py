# Chapter 5: Dictionaries and Structuring, Page Number: 127

# In this chapter, we used the dictionary value {'1h': 'bking', '6c': 'wqueen',
# '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'} to represent a chess board.

# Write a function named isValidChessBoard() that takes a dictionary argument and returns True or False depending on if the board is valid.

# A valid board will have exactly one black king and exactly one white king.
# Each player can only have at most 16 pieces, at most 8 pawns, and all pieces must be on a valid space from '1a' to '8h';
# that is, a piece can’t be on space '9z'.
# The piece names begin with either a 'w' or 'b' to represent white or black, followed by 'pawn', 'knight', 'bishop', 'rook',
# 'queen', or 'king'. This function should detect when a bug has resulted in an improper chess board.


def isValidChessBoard(check_chess: dict) -> bool:

    # creating a list of all the valid positions
    valid_positions = []
    for i in range(1, 9):
        for j in range(97, 105):
            valid_positions.append(str(i) + chr(j))

    # list of all valid pieces
    valid_pieces = [
        "wpawn",
        "wknight",
        "wbishop",
        "wrook",
        "wqueen",
        "wking",
        "bpawn",
        "bknight",
        "bbishop",
        "brook",
        "bqueen",
        "bking",
    ]

    # checking if the chess board is valid
    for position in check_chess:

        if position not in valid_positions:
            return False
        if check_chess[position] not in valid_pieces:
            return False

    return True


test = isValidChessBoard(
    {"1h": "bking", "6c": "wqueen", "2g": "bbishop", "5h": "bqueen", "3e": "wking"}
)
print(test)
