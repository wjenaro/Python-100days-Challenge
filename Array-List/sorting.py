myList=[3,1, 92, 4,57,8,2, 32]
l=len(myList)

for i in range(l):
    for n in range(0, l-i-1):
        if myList[n] > myList[n+1]:
            myList [n], myList[n+1]= myList[n+1] , myList[n]
print(myList)