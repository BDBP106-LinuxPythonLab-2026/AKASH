from encodings import cp037

angle=float(input("Enter angle in Degrees ; "))
#since noe you need to do a bit of maths so call the math module remember you learnt it pehle

import math
rad=math.radians(angle)

sin=math.sin(rad)
cos=math.cos(rad)
tan=math.tan(rad)

sec=1/cos
cosec=1/sin
cot=1/tan

print("sin=",sin)
print("cos=",cos)
print("tan=",tan)
print("cot=",cot)
print("sec=",sec)
print("cosec=",cosec)
