emojis = ["😀", "😃", "😄", "😁", "😆", "😅", "😂", "🤣", "😊", "😇", "🙂", "🙃", "😉", "😌", "😍", "🥰", "😘", "😗", "😙", "😚", "😋", "😛", "😜", "🤪", "😝", "🤑", "🤗", "🤭", "🤫", "🤔", "🤐", "🤨", "😐", "😑", "😶", "😏", "😒", "🙄", "😬", "🤥", "😌", "😔", "😪", "🤤", "😴", "😷", "🤒", "🤕", "🤢", "🤮", "🤧", "🥵", "🥶", "🥴"]

print(emojis)
print(len(emojis))
chess_board = [
    ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"],
    ["♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙"],
    ["X", "X", "X", "X", "X", "X", "X", "X"],
    ["X", "X", "X", "X", "X", "X", "X", "X"],
    ["X", "X", "X", "X", "X", "X", "X", "X"],
    ["X", "X", "X", "X", "X", "X", "X", "X"],
    ["♟", "♟", "♟", "♟", "♟", "♟", "♟", "♟"],
    ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"],
]

for row in chess_board:
    for piece in row:
        print(piece, end=" ")
    print()


import random

row1 = ["▪️", "▪️", "▪️", "▪️"]
row2 = ["▪️", "▪️", "▪️", "▪️"]
row3 = ["▪️", "▪️", "▪️", "▪️"]
row4 = ["▪️", "▪️", "▪️", "▪️"]

random_row = random.choice([row1, row2, row3, row4])
portion = random_row[:1]  # Select the first two elements from the randomly chosen row

print(portion)
print("================================================ii========================================")

#create a cheese board
import random
def theboard():
    row1 = ["▪", "▪️", "▪️", "▪️"]
    row2 = ["▪️", "▪️", "▪2", "▪️"]
    row3 = ["▪️", "▪️", "▪️", "1"]
    row4 = ["▪️", "▪️", "▪️","o", "▪"]

    return [row1, row2, row3, row4]

    
def guess():
    board=theboard()
    computerguess=random.choice(board)
    random_position = random.randint(0, len(computerguess) - 1)
    print(random_position)
guess()