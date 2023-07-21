#create a cheese board
import random
def theboard():
    row1 = ["▪", "▪️", "▪️", "▪️"]
    row2 = ["▪️", "▪️", "▪️", "▪️"]
    row3 = ["▪️", "▪️", "▪️", "▪️"]
    row4 = ["▪️", "▪️", "▪️", "▪"]

    return [row1, row2, row3, row4]

    
def guess():
    board=theboard()
    computerguess=random.choice(board)
    
    random_position = random.randint(0, len(computerguess) - 1)
    computerguess[random_position] = "😃"

    return board


result = guess()
for row in result:
    print(row)



