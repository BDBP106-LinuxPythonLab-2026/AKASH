a=float(input("enter length of side 1:"))
b=float(input("enter length of side 2"))
c=float(input("enter length of side 3"))

if a==b and b==c:
        print("The triangle is Equilateral")
elif a==b or b==c or c==a:
        print("The triangle is Isoceles")
else:
        print("The triangle is not Scales")
