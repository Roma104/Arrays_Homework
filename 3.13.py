###
#Define a function occurs(number, array) that returns True if a given number is present in an array. 
# Then create a program that checks whether the number entered from the keyboard is present in the array [15, 38, 7, 23, 14].
#

def occurs(number, array):
    for i in array:
        if i == number: return True
    return False

arr = [15, 38, 7, 23, 14] 
nr = int(input("Podaj numer: "))
print(f"{nr} appears in the array: {occurs(nr, arr)}")