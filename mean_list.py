"""WAP to calculate mean of a given list of numbers. """

#Input
n=int(input("Enter the number of elements to be inserted: "))
a=[] #Making a list to store  elements
for i in range(0,n):
    elem=int(input("Enter element: "))
    a.append(elem) #Append() function used to insert element in the end of list
avg=sum(a)/n   #Sum() function is used
print("Average of elements in the list",round(avg,2))
