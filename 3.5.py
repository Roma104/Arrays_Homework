###
#An array contains values: 15, 8, 31, 47, 2, 19. 
# Create a program that calculates and prints the array and the arithmetic mean of array values. 
# Use the “for” loop statement.
#

array = [15, 8, 31, 47, 2, 19]
sum = 0

for i in array:
    sum += i

print(array)
print("Arithmetic mean: ", sum/len(array))