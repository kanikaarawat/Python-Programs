"""WAP to print odd numbers and sum of odd numbers from the list."""
#Inputting elements separated by space so that we can split them into list
input_string = input("Enter a list element separated by space:")

#Using split function
l1  = input_string.split()
sum1=0

#Odd numbers are found int the list
for num in l1:
    if int(num)%2!=0:
      sum1+=int(num)  
      print(num,end=" ")    
print("\nThe sum of numbers:",sum1)
