###
#An array contains integer numbers: 2, 6, 4, 9, 7. 
# Create a program that prints the array values graphically as below. 
# Define a function star(n) that returns the given number of asterisks as a string.
# Use a defined function in the program.
#

arr = [2,6,4,9,7]

def star (arr):
    for i in arr:
        print(i, end=": ")
        for j in range(i):
           print("*", end="")
        print()
       
    return arr


print (star(arr))