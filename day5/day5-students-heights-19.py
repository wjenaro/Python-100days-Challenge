import random

student_heights=[random.randint(150, 180) for _ in range(20)]
#get student avarage height

sum=0
for height in student_heights:
    sum+=height

avarage_height=sum/len(student_heights)
print(avarage_height)
