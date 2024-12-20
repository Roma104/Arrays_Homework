#min max 
#An array contains numbers: -15, 8, -31, 47, -2, 19. 
# Create a program that finds and prints the maximum and minimum number. 
# Do not use available functions.

def largest(arr, n):
 

    max = arr[0]
 

    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max
 
 

arr = [-15, 8, -31, 47, -2, 19]
n = len(arr)
Ans = largest(arr, n)
print( Ans)