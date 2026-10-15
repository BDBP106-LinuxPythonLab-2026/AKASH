text="Hello World 2026"

text=text.lower()
vowels=0
consonants=0
digits=0
spaces=0

for c in text:
    if c in "aeiou":# this is called membership withing i guess
      vowels+=1
    elif c.isalpha():  #isalpha is a method so use c. before it , otherwise won't work
        consonants+=1
    elif c.isdigit():
        digits+=1
    elif c==" ":
        spaces+=1
    else:
        print("END")

print(vowels,consonants,digits,spaces)



