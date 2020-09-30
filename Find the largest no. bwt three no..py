a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if a>=b and a>=c:
   largest=a
elif b>=c and b>=a:
   largest=b
else:
   largest=c
print("The largest number between", a, ",", b, "and", c, "is", largest)