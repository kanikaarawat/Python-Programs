"""WAP to find minimum element from the list."""
list1 = list(eval(input("Enter the elements of list separated by comma:")))#eval converts the input to tuple hence list() used
list1.sort() #tuple can't use sort hence list() used
print("Smallest element is:", list1[0]) #Gives first element
