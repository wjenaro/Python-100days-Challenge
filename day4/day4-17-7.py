import random
 
#method to create a stone
def stone():
    size = 10  

    for i in range(size):
        spaces = " " * (size - i - 1)
        stars = "*" * (2 * i + 1)
        print(spaces + stars)

    for i in range(size - 2, -1, -1):
        spaces = " " * (size - i - 1)
        stars = "*" * (2 * i + 1)
        print(spaces + stars)

#scissors
def scissors():
    size = 10  

    for i in range(size):
        if i < size // 2:
            spaces = " " * i
            stars = "*" * (size - i * 2)
            print(spaces + stars + spaces)
        elif i == size // 2:
            print("*" * size)
        else:
            spaces = " " * (size - i - 1)
            stars = "*" * ((i * 2) - size + 2)
            print(spaces + stars + spaces)
#paper
def paper():
    size = 10  

    for i in range(size):
        if i == 0 or i == size - 1:
            print("*" * size)
        else:
            spaces = " " * (size - 2)
            print("*" + spaces + "*")

#random selection 
def randomSelection():

    # prints a random value from the list
    numbers_for_selection = [0, 1, 2]
    return random.choice(numbers_for_selection)

usern=int(input("Give a number between 0-2: "))
#user number selection -- select between 0, 1, 2
#play game
def playGame(userChoice):
    computerChoice=randomSelection()
    if computerChoice==0 and userChoice ==0:
        print("Computer---->")
        stone()
        print("User===>")
        stone()
    elif computerChoice==0 and userChoice ==1:
        print("Computer---->")
        stone()
        print("User===>")
        paper()
    elif computerChoice==0 and userChoice ==2:
        print("Computer---->")
        stone()
        print("User===>")
        scissors()
        
    elif computerChoice==1 and userChoice==0:
        print("Computer---->")
        paper()
        print("User---->")
        stone()
    elif computerChoice==1 and userChoice==1:
        print("Computer---->")
        paper()
        print("User---->")
        paper()
    elif computerChoice==1 and userChoice==2:
        print("Computer---->")
        paper()
        print("User---->")
        scissors()
    elif computerChoice==2 and userChoice==0:
        print("Computer---->")
        scissors()
        print("User---->")
        stone()
    elif computerChoice==2 and userChoice==2:
        print("Computer---->")
        scissors()
        print("User---->")
        scissors()
    elif computerChoice==2 and userChoice==1:
        print("Computer---->")
        paper()
        print("User---->")
        scissors()
    
        '''let points for the items ---
        stone --- 1 point. 
        paper --- 2 points
        scissors--- 3 points 
        ---if same as computer 10 points

        '''
    #assign values 
    st=1
    pa=2
    sc=3
    

    if userChoice==computerChoice:
        print("Congrat ===You Won with == 10 points ")

    elif userChoice==0:
        print("You lost")
        if computerChoice==1:
            print("Your points are :"+str(st-pa) +" Points")
        elif computerChoice==2:
            print("You Lost")
            print("your points are :"+str(st-pa)+" Points")
    elif userChoice==1:
        if computerChoice==0:
            print("You Won narrowly  -- You can do better")
            print("your points are :"+str(pa-st)+" Points")
        elif computerChoice==2:
            print("You Lost")
            print("your points are :"+str(pa-st)+" Points")

    elif userChoice==2:
        if computerChoice==0:
            print("You won")
            print("your points are :"+str(sc-st)+" Points")
        if computerChoice==1:
            print("You won")
            print("your points are :"+str(sc-pa)+" Points")

playGame(usern)#play game0