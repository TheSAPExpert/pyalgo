""""
1. Determine even numbers in table
2. Determine smallest value in table
3. Determine biggest value in table
4. Create greatest and lowest functions
5. Create a function that extracts greatest and lowest

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

#Function that returns the greater or lower value of two depensds on desc param
def compare(firstVal, secondVal, desc=True):
    if (desc):
        return getLowerOf(firstVal,secondVal)
        
    return getGreaterOf(firstVal, secondVal)


#Function that extracts greatest and lowest of array
def extractorMax&Min(maxVal,minVal):



# My table
array = [15, 3, 25, 10, 7, -15, 43, 2, 4, 6]

# Initialise .. as the first item in the array
maxVal = array[0]

# iterating each number in list starting at second element
for num in array[1:]: 
      
    # find in array using While Loop
        maxVal = getGreatestOf(maxVal,num)

# Print the Value
print(maxVal)
