print("1.Calculate Area of Square")
print("2.Calculate Area of Triangle")
choice=int(input("Enter your Choice(1 or 2):"))
if choice==1:
    side=float(input("Enter length of side:"))
    print("Area of Square=", side**2)
elif choice==2:
    base=float(input("Enter length of Base:"))
    height=float(input("Enter length of Height:"))
    print("Area of Triangle=", 1/2*base*height)
else:
    print("Wrong Choice....\nTry Again")