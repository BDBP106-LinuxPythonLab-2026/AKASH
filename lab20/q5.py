# #Build a menu-driven program that keeps running until the user picks Quit:
# 1. Add item 2. Remove item 3. View list 4. Sort list 5. Quit
# Don't add duplicates (check case-insensitively). Print a friendly message when the user
# tries to remove an item that isn't on the list. Show the list numbered from 1.

L=[]



print("Welcome Customer", "What would you like to do ")
q=input("Type 'menu' to get MENU :")
if q=="menu":
    print("Add item  -a", "Remove item  -b", "view list  -c", "sort list   -d", "Quit  -e", sep="\n")

user=input("choose Operation to be performed:")
if user=="a":
    a=input("Write item name :")
    L.append(a)
    print("item added")
elif user=="b":
    b=input("Write item name :")
    if b in L:
        L.remove(b)
    else:
        print("Sorry, the item selected is not listed")

elif user=="c":
    if i, item in enumerate(L,1):
        print(i,item)

elif user=="d":
    L.sort()
    print(L)
elif user=="e":
    print("QUIT")
else:
    print("ERROR")




