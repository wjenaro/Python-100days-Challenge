import random
#generate word
word=''
filename="Day7 -Hangman Challenge\words.txt"
with open(filename, "r") as f:
    words = f.read().split(",")
    random_index = random.randint(0, len(words) - 1)
    word= words[random_index].strip() #use strip method to remove space 
#determine the number of words in the word
number_of_letters=len(word)
#create dash list( black spaces to fill )
blank_spaces=[]
for i in range(number_of_letters):
    blank_spaces.append(" _ ")
#print the word and corresponding dashes
print(word)
print(blank_spaces)

#start the game - iterate until all the letter are filled in the dashes ... 
#number of lives is equal to number of letters
lives=number_of_letters #I know it is not needed but it is okey --- just practicing 
#use while 
myword=word.lower()
while lives>0:
    #guess letter
    my_guess=input("Guesss a letter in the word: __ ")
    print(f"My guess is __: {my_guess}")
    if my_guess in word.lower(): 
        print(" You saved Live")
        for position in range(number_of_letters):
            letter=myword[position]
            if my_guess==letter:
                blank_spaces[position]=letter
        print(blank_spaces)
    else:
        print("You lost Live")
    lives-=1

