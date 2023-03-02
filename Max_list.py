"""WAP to find maximum element from the list"""
list1 = list(eval(input("Enter the elements of list separated by comma:")))
list1.sort() 
print("Largest element is:", list1[-1])
