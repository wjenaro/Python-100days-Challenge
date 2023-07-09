def createList(num1: int, num2: int, *args) -> list[int]:
    mylist=[num1, num2, *args]
    return mylist


result = createList(3, 5, 7,6,7,2,9,4,34)
print(result) 
