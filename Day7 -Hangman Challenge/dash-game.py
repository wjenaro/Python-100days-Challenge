#replace dashes with letter if guess was right  
#guess the world from the txt
import random
my_guess=''
filename="Day7 -Hangman Challenge\words.txt"
with open(filename, "r") as f:
    words = f.read().split(",")
    random_index = random.randint(0, len(words) - 1)
    my_guess= words[random_index]
print(my_guess.strip())
number_of_letter=len(my_guess.strip())
print(number_of_letter)
dashes=[]
#generate dashes
for i in range(number_of_letter):
    dashes.append("_")
print(dashes)

#guess letter in the word
word=my_guess.strip()
for w in range(number_of_letter):
    print(w)
my_guess_letter=input("Guess letter :")
if my_guess_letter in my_guess.strip():
    print(" the letter is in the world")
else:
    print("the letter not in the word")
