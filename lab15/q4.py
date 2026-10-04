import math

a = float(input("Enter a number: "))
b = float(input("Enter another number: "))
c = float(input("Enter another number: "))


D= b*b -4*a*c
print(math.sqrt(D))

root1= (-b + math.sqrt(D) ) /  (2*a)
root2= (-b - math.sqrt(D) ) /  (2*a)

print("root 1 is :" ,root1)
print("root 2 is :", root2)
