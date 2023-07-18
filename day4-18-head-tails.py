#this is  a game 
import random
#function to get a head or tai
def coinToss():
    numbers =[0,1]
    return random.choice(numbers)
def hOrt():
    randomnumber=coinToss()
    if randomnumber==0:
        print("Heads")
    else:
        print("Tails")

hOrt()


