#By-Tuhin
suba=int(input("Enter Subject 1 marks:"))
subb=int(input("Enter Subject 2 marks:"))
subc=int(input("Enter Subject 2 marks:"))

if suba>100:
    print("Subject 1 marks exceding 100")
    
if subb>100:
    print("Subject 2 marks exceding 100")
    
if subc>100:
    print("Subject 3 marks exceding 100")
    
if suba>100 or subb>100 or subc>100:
    print("Try again")

else:
    print("You got", suba+subb+subc, "out of 300 in all subject")