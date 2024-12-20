###
#Create a program that sorts elements of an array containing integer numbers. 
# Apply the Bubble Sort sorting algorithm. 
# Define a function bubblesort(array) that returns the sorted array. 
# Try to sort and print any three arrays.
#

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


arr1 = [5, 6, 2, 4, 89, 23, 11, 0, 1, -1, 234, 123, 1]

arr2 = [-1, 0, 5, 7, 2, -1]

arr3 = [5, 4, 3, 2, 1, 0]

print('For arr 1')
print(arr1)
print(bubbleSort(arr1))
print('For arr 2')
print(arr2)
print(bubbleSort(arr2))
print('For arr 3')
print(arr3)
print(bubbleSort(arr3))