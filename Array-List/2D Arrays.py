myMatrix=[
    [1,2,3,4],
    ['one','two', 'three', 'four'],
    ['moja', 'mbili', 'tatu', 'nne']
]

print(myMatrix[0][1])

#
for row in myMatrix:
    for element in row:
        print (element, end=" ")
    print("")