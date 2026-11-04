sentence=input("Enter a sentence:")

words=sentence.split()

#unique_words=set(words)
#print(unique_words)
#with this we r not getting in sequence

D={}
for word in words:
    D[word]=1
for word in D:
    print(word,end= " " )




