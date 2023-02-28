"""Extract two list-slices out of a given list of numbers. Display and print the sum of elements of first list-slice which contains every element of the list between indexes 5 to 15.
Program should also display the average of elements in second list that contains every fourth element of the list."""
#Input elements in list
l = list(input("Enter the elements for a list:"))

#Slicing elements into a sublist
s1=l[5:11:2]
print("Elements of 1st slice:",s1)

#Addition of elements of sublist
sum1=0
for i in s1:
    sum1+=int(i)          #Type casting since we need to add str i and int sum1
print("Sum of elements of the 1st slice:",sum1)

#A sublist with every fourth element
s2=l[::4]

#Average 
sum1=avg=0
length=len(s2)
print("Elements of 2nd slice:",s2)
for x in s2:
    sum1+=int(x)             #Type casting since we need to add str i and int sum1
avg=sum1/length
print("Average of elements of 2nd slice:",avg)

