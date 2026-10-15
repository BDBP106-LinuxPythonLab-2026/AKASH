a=17
b=int(input("Guess the number :"))
count=0

while True:
    if b>a:
        print("Too High")
        print("Guess again")
        count+=1
        b = int(input("Guess the number :"))

    elif b<a:


        print("Too Low")
        print("Guess again")
        count+=1
        b = int(input("Guess the number :"))
    else:
        print("FOUND")
        count+=1

        print("Total count of attempts to match the final answer :", count)
        break

    if count==7:
        print("STOP MORE THAN 7 ATTEMPTS")
        print("Number is",a)
        break




