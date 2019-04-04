""""
1. Determine even numbers in table
2. Determine smallest value in table

"""
# My table
array = [15, 3, 25, 10, 7, -15, 43, 2, 4, 6]

# Initialise the min as the first item in the array
minVal = array[0]

# iterating each number in list starting at second element
for num in array[1:]: 
      
    # find minimum in array using While Loop
    if num < minVal:
        minVal = num

# Print the minValue
print(minVal)