"""WAP to print negative numbers and sum of odd numbers from the list."""
#Inputting elements separated by space so that we can split them into list
input_string = input("Enter a list element separated by space:")

#Using split function
l1  = input_string.split()
#Sum of positive numbers from list
sum1=0
for num in l1:
       if int(num)<0:          #type casting so that same data type can be compare
          sum1+=int(num)       #typecasting since num is not int but str
          print(num,end=" ")
print("\nThe sum of numbers:",sum1)
