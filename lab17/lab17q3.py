N=int(input("Give a Number:"))

for i in range( 2 ,N ):
    if N%i==0:
     print("Not Prime")
     break

else:
    print("Prime")