#Input items in list
#Importing module colorama to change text while displaying
import colorama
list1=list(input("Enter the elements for the list:"))
#Displaying elements in separate lines with positive indexes
from colorama import Fore,Back
print(Fore.WHITE+Back.BLACK+"The elements in positive indexes")
for i in list1:
      print(i)
#Displaying elements in separate lines with negative indexes
print(Fore.WHITE+Back.BLACK+"The elements in positive indexes")
for i in list1[::-1]:
      print(i)
