def leapYear(year):
    if year%4==0:
       
        if year%100!=0:
            print("leap year ----")
        elif year%400==0:
            print("leap year --last test")
        else:
            print("not leap")
    else: 
        print("not leap year last check")


year=int(input("Guess a year to test "))
leapYear(year)