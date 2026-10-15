# 7. Word Frequency Counter
# Concepts: dictionaries, split(), strip(), lower(), get(), items()
# Read a paragraph. Count how often each word appears, ignoring case and stripping
# surrounding punctuation (.,!?;:). Print the words alphabetically with their counts. Then
# print the most frequent word. If several words tie, print all of them.

para= "Python is easy, and Python is powerful! I like Python because Python is fun. Coding is fun, too!"

words=para.split()
print(words)
highest=0
counts = {}    #creating a Dictionary so that it can save the word how many times its getting repeated

for word in words:       #word is for eah element iterating
    word = word.strip(".,!?;:")
    word = word.lower()

    counts[word] =counts.get(word,0) + 1    #count is the DIct , now .get will tell whats the element which include 2 things,counts[word] means us word ka count is =
print("Word Frequesncies :",counts)

print("------- Starts----------")
for name , rep in sorted(counts.items()):
    print(name,":",rep)
print("---------Ends-----------")
for name,rep in counts.items():    #is loop me hamne sirf highest find kiya hai , dont print the valuse otherwise tie wale wont be printed
    if rep > highest:
        highest = rep
        print("No. of times repeated =",rep)

    if rep == highest:
        print("with highest frequency =", name,":",highest)




