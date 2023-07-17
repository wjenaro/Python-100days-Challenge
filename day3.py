'''
Wrie a progrm that inteprets the Body Mass Index (BMI) based on a user's 
weight and height.
 it should tell them the intepretation of their BMI based on the BMI value.
 >Under 18.5 they are underweight 
 >over 18.5 below 25 they have normal weight 
 >over 25 but below 30 thy are overweight
 >over 30 but below 35 they are obese 
 >above 35 they are clinically obese 98

 BMI Formula: weight (kg) / height (m2)
'''
def calculateBMI(weight, height) -> float:
    return weight/height**2
yw=float(input("Your Weight:  " ))
yh=float(input("Your height is: "))
#calculate BMI
bmi=calculateBMI(yw,yh)
#interprete BMI
if bmi<18.5:
    print(f"With {str(bmi)} it means you are Underweight")
elif bmi>= 18.5 and bmi<25:
    print(f"With {str(bmi)} it means you have Normal weight for you height")
elif bmi>= 25 and bmi<30:
    print(f"With {str(bmi)} it means you have Normal weight for you height")
elif bmi>= 30 and bmi<35:
    print(f"With {str(bmi)} it means you are obese for you height")
else:
    print(f"With {str(bmi)} it means you are climically obesse for you height")

from datetime import date

today = date.today()
print("Today's date:", today)