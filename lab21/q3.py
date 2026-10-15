import math

def f(angle):
    x=math.sin(math.radians(angle))
    y=math.cos(math.radians(angle))
    return(x,y)

print(f(30))

angle=(30,60,90)
print(list(map(lambda angle: ( math.sin(math.radians(angle)), math.cos(math.radians(angle))),angle)))


