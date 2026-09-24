import math

a=float(input("enter the number a:"))
b=float(input("enter number b:"))
c=float(input("enter number c:"))

D=b*b-4*a*c
root1=(-b-math.sqrt(D))/(2*a)
root2=(-b+math.sqrt(D))/(2*a)

print("Root 1 is :",root1)
print("Root 2 is :",root2)