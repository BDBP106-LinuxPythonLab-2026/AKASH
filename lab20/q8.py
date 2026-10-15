python_class = ["Anil", "Bina", "Chetan", "Deepa", "Anil", "Esha"]
java_class = ["Chetan", "Farhan", "Deepa", "Gita", "Bina"]

#py = sorted(set(python_class)) #sorted karne ke baad answer ek """list"""" me hota hai , remember that , its not a set now !
py = (set(python_class))
java = (set(java_class))

print(py)
print(java)
print("Both subjects :",py & java)
print("Only python :",py - java)
print("Taking only One course :",py ^ java)  #taking only one course so more like [( py +java ) - there intersection]
print("every unique student :",sorted(py | java)) #every unique student they need it means uninon of all - since its a set , repetition wont be seen , but they also need it as sorted so just add sorted infront of them.

a=input("Enter student's name:")


if a in py:
    if a in java:                            #make sure to use the nested if ka logic i dont remeber kaha seekha b ut useful it is !!
        print("Student :",a ,"in both course python & java")
    else:
        print("Student :", a, "course python")
if a not in py and a not in java:                # make sure to remember the synatx of isme bhi na ho usme bhi na ho ka , important it is !!!
    print("Student not found ")

