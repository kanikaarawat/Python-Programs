"""WAP to accept the cost price of a bike and display the road tax to be paid according to the following criteria:"""
cost=float(input("Enter cost of your bike:-"))
if cost>100000:
    print("15% tax to be paid")
elif cost>50000 and cost<=100000:
    print("10% tax to be paid")
elif cost<=50000:
    print("5% tax to be paid")

