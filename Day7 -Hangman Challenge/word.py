import random

def generate_random_word(filename):
  with open(filename, "r") as f:
    words = f.read().split(",")
    random_index = random.randint(0, len(words) - 1)
    return words[random_index]
def num_of_letters(word):
  return len(word)-1


 

def main():
  filename = "/home/coder/Desktop/day-challenge/Python-100days-Challenge/Day7 -Hangman Challenge/words.txt"
  word = generate_random_word(filename)
  print(word)
  print("Number of letter in the word: "+str(num_of_letters(word)))
  for i in range(num_of_letters(word)):
    print(" - ", end="")
  print()
  


if __name__ == "__main__":
  main()

