"""WAP to search for an element in a given list of numbers."""
#Input
a=input('enter the list:')
b=input('enter the number to be found')
#Process (for loop)
if b in a: #keyword in is used
    print("The desired number is in the list at index",a.index(b))#list.index() function is used 
else:
    print("The number not found")
