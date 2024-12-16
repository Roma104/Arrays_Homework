###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print('Last value', arr[-1])
print('Las but one value, no negative indext', arr[3])

sum = arr[0] + arr[-1]
print('Sum of first and last value', sum)

print('Middle value', arr[2])

print('Array values:', end=' ')
for value in arr:
    print(value, end=' ')
print()