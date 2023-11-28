letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
text=input("Enter text to be encrypted:\n").lower()
shift=int(input("Enter shift number: \n"))

def encrypt(plain_text, s):
    new_text =[]  
    for i in plain_text:
        position=letters.index(i)
        new_position=position+s
        new_text.append(letters[new_position])
        
    print("".join(new_text))

        

      

encrypt(text, shift)