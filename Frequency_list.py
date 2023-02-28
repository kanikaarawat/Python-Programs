"""
WAP to count frequency of a given element in a list of numbers.
                                                               """

l=eval(input("Enter List separated by comma:")) #eval() function used to get comma separated elements in a list.
length=len(l)
element=int(input("Enter the element:"))
c=0
for i in range(0,length):             #Checking each element using for loop
    if element==l[i]:
        c=c+1
if c==0:
    print("Not found")
else:
    print("The frequency of {0} in the list is: {1}".format(element,c))  
                                      #format() function used for displaying values of two variables
