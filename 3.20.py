###
#Write a program to separate even and odd numbers of a given array of integers. 
# Put all even numbers first, and then odd numbers.
#

arr = [7,9,2,4,5,6]

parzyste = []
nieparzyste = []

for i in arr:
    if i % 2 ==0:
        parzyste.append(i)
    else:
        nieparzyste.append(i)



arr = parzyste + nieparzyste

print(arr)       