###
# Write a program that checks whether the first array is a subset of the second one 
# (whether all elements of the first array appear in the second array).

arr1 = [1, 2, 3]
arr2 = [1, 2, 3, 4, 5]

print(set(arr1).issubset(arr2))