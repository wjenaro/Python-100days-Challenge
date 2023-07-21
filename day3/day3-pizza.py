piz=input("What size : ")
cost=0
if piz=="sm":
    print("Pay $15")
    cost=15
elif piz=="m":
    print('pay $ 20')
    cost=20
elif piz=="l":
    print('pay $25')
    cost=25
pp=input('Do you want pepperoni:y/n ')

if pp=="y" and piz=='sm':
    cost+=2
if pp=="y" and piz=='m':
    cost+=3
if pp=="y" and piz=='l':
    cost+=3
print("You will pay :$"+str(cost))
extr=input('Do you want extra cheese? y/n: ')
if extr=="y":
    cost+=1
print("The total cost is :$"+str(cost))


 