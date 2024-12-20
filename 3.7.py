###
#Create a program that prints the longest name (consisting of the largest number of characters).
#

array = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
array = sorted(array, key=len, reverse=True)
print(array)
print("Longest name: ", array[0])