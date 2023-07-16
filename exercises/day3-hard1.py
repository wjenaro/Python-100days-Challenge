def calculate_love_score(name1, name2):
    true_count = count_letters(name1 + name2, 'TRUE')
    love_count = count_letters(name1 + name2, 'LOVE')
    love_score = int(str(true_count) + str(love_count))
    return love_score

def count_letters(text, word):
    count = 0
    for letter in word:
        count += text.upper().count(letter)
    return count

# Get names from user
name1 = input("Enter the first person's name: ")
name2 = input("Enter the second person's name: ")

# Calculate love score
score = calculate_love_score(name1, name2)

# Display the love score
print(f"The love score between {name1} and {name2} is {score}%.")


