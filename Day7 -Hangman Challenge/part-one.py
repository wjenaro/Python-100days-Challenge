import random
word_list=['Mama', 'Papa', 'House']
#print(len(word_list))

#select random word.
random_word_id= random.randint(0, len(word_list)-1)

#print(random_word_id)

#the selected string
myword=word_list[random_word_id]
print(myword)
#the length of my word
print(len(myword))
#convert to string
#print(myword)
#check letter in the word
letter=input("guess letter: ").lower()
#print(len(myword))

if letter in myword.lower():
    print (" you won")
else:
    print("lost")

