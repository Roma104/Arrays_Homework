###
#A two-dimensional array of the size 3 by 5 contains integer numbers. 
# Create a program that swaps the first and the last column. 
# Print array values in rows and columns before and after changes.
#

arr = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5]
]

for i in arr:
    for j in i:
        print(j, end=" ")
    print()

for i in arr:
    i[0], i[4] = i[4], i[0]

print("==========")
for i in arr:
    for j in i:
        print(j, end=" ")
    print()