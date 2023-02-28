"""WAP to accept a number from 1 to 7 and display the name of the day like 1 for Sunday, 2 for Monday...."""
Day = int (input("Enter the day of the week:"))
if Day==1:
        print("It is Monday")
elif Day==2:
        print("It is Tuesday")
elif Day==3:
        print("It is Wednesday")
elif Day==4:
        print("It is Thursday")
elif Day==5:
        print("It is Friday")
elif Day==6:
        print("It is Saturday")
elif Day==7:
        print("It is Sunday")
else:
        print("It is an invalid input")
