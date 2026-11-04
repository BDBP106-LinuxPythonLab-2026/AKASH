import math

#a=input("Enter a :")
#b=input("Enter b :")
#c=input("Enter c :")

def area_function (a,b,c):
 s=(a+b+c)/2
 print(s)
Area= math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of square:",Area)

area_function(3,2,4)