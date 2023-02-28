""" WAP to accept percentage from the user and display the grade according to the criteria"""
per=float(input("Enter your percentage:-"))
if per>90:
    print("Grade A")
elif per>80 and per<=90:
    print("Grade B")
elif per>=60 and per<=80:
    print("Grade C")
else:
    print("Grade D")
