#develop a tip calculator 
print('Welcome to the tip calculator')
billS=input("What is the total bill? ")
numberOfPS=input("How many people to split the bill?  ")
tipS=input("What percentage are willing to give? 10, 12, 15 ")
'''
rel calculator

'''
bill=float(billS)
numberOfP=int(numberOfPS)
tip=int(tipS)

if tip==10:
    pay= (bill*1.1)/numberOfP
    print(f"Each person is supposed to pay: ${str(round(pay, 1))}")
elif tip==12:
    pay= (bill*1.12)/numberOfP
    print(f"Each person is supposed to pay: ${str(round(pay, 1))}")
elif tip==15:
    pay= (bill*1.15)/numberOfP
    print(f"Each person is supposed to pay: ${str(round(pay, 1))}")