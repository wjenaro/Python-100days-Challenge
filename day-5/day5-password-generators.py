#
print("Welcome to create a password")

'''
input untill the condition is met. 

'''
num_of_characters = 0

while True:
    num_of_characters = int(input("Give the number of characters: "))
    if num_of_characters >= 8 and num_of_characters <= 20:
        break
    else:
        print("Please enter a number between 8 and 20.")



'''
numbers 
'''
capital_letters = [chr(x) for x in range(65, 91)]
small_letters =   [chr(x) for x in range(97, 123)]
special_characters = [chr(x) for x in range(33, 48)] + [chr(x) for x in range(58, 65)] + [chr(x) for x in range(91, 97)] + [chr(x) for x in range(123, 127)]
numbers_ = [str(x) for x in range(0, 10)]
# Print the lists
#random 
import random
'''
at least one character is capital , at least no  character is number and at least two special characters. 
must be at least eight characters

'''
randomCapital=random.choices(capital_letters)
random_small=random.choices(small_letters, k=3)
random_special=random.choices(special_characters, k=2)
random_num=random.choices(numbers_, k=2)
pass_list=[]
if num_of_characters==8:
    pass_list=randomCapital+random_special+random_num+random_small
else:
    remainin=num_of_characters-8
    remain_char=random.choices(small_letters, k=remainin)
    pass_list=remain_char+randomCapital+random_special+random_num+random_small

mypassword=''.join(pass_list)

print(mypassword)
    
    
