###
#A two-dimensional array of the size 3 by 5 contains integer numbers. 
# Create a program that swaps the first and the last row. 
# Print array values in rows and columns before and after changes.
#

arr = [[1, 8, 4, 0, 10],
       [60, 50, 40, 50, 100],
       [5, 5, 5, 5, 5],
      ]

print("Tablica:")
print (arr)
       
arr[0], arr[2] = arr[2], arr[0]

print("Tablica po zamianie:")
print(arr)