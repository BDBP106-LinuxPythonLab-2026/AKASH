a=int(input("Enter an Integer :"))

if a>0:
    print("Positive")
    if a%2==0:
        print("Even")
    else:
        print("Odd")

elif a<0:
    print("Negative")
    if a%2==0:
        print("Even")
    else:
        print("Odd")

else:
    print("ZERO")

if a%3==0 and a%5==0:
    print("Frizzbuzz")
else:
    print("Not Divisible")