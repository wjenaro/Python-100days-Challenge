#generate passord
import random
pass_length=int(input(" Give the length of pass: "))
num=[str(i) for i in range(10)]
alphabets_list = [chr(i) for i in range(ord('a'), ord('z')+1)] + [chr(i) for i in range(ord('A'), ord('Z')+1)]
special_characters_list = [chr(i) for i in range(33, 127) if not chr(i).isalnum()]
#concatenate the lits
password_list=num+special_characters_list+alphabets_list

generated_password= random.choices(password_list, k=pass_length)

print(''.join(generated_password))

