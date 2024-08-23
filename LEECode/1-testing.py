# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
nums = [2,7,11,15]
target=9
output=[]

l=len(nums)
for i in range(l-1):
    nu=nums[i]+ nums[i+1]
    if nu==target:
        output.append(i)
        output.append(i+1)
        print(output)
        