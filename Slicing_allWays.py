"""Trying all ways to slice a list"""
a=[1,2,3,4,5,89,75,9,6]   #This is the input list
n=len(a)                  #len() function used for finding length.
print(a[::])              #This will print the default list since start and end is not given.
print(a[::2])             #This will print the default list while leaving one element in between.
print(a[1::3])            #This will print the list with index 1 while leaving 2 elements in between.
print(a[::-1])            #This will print the list in reversed order.
print(a[-3:])             #This will print the list from index -3 to index -1 since end point/step gap taken as by default one.
print(a[-2:-n])           #This will print an empty list since -1 as step count is not given.
print(a[-2:-n:-1])        #This will print the list from index -2 to the second element.
print(a[::-2])            #This will print the list in reverse order while leaving one element in between.


