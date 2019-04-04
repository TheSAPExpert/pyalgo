""""
1. Determine even numbers in table
2. Determine smallest value in table
3. Determine biggest value in table
4. Create a 

"""
#Function returns lowest value of two params
def getLowerOf(firstVal, secondVal):
    if firstVal < secondVal :
        return firstVal
    else:
        return secondVal

#Function returns the greatest value of two params
def getGreatestOf(firstVal, secondVal):
    if firstVal > secondVal :
        return firstVal
    else:
        return secondVal

# My table
array = [15, 3, 25, 10, 7, -15, 43, 2, 4, 6]

# Initialise the min as the first item in the array
maxVal = array[0]

# iterating each number in list starting at second element
for num in array[1:]: 
      
    # find minimum in array using While Loop
    if num > maxVal:
        maxVal = num

# Print the minValue
print(maxVal)