S=input("Enter Your Sentence :")
W=input("Enter Your desired Word :")

words=S.split()
count=0
for i in words:
   if i==W:
    count=count +1
print("Occurrence :",count)
