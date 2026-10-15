

n=int(input("Enter a Number:"))
a=0
b=1

for i in range(1,n+1):
    if a%2 !=0:
        print("odd:",a)

    c=a+b
    a=b
    b=c


