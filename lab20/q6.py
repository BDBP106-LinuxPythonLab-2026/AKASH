# #Concepts: list of tuples, tuple unpacking, for, if/elif grading, max/min by manual
# tracking
# Start with:
# students = [("Asha", 88), ("Ravi", 72), ("Meera", 95), ("Karan", 59), ("Divya", 81)]

# Print each student's letter grade (A ≥ 90, B ≥ 80, C ≥ 70, D ≥ 60, otherwise F). Then print
# the class average and the top and bottom scorers. Find the top and bottom scorers with
# a loop, not with max() and a key.

students = [("Asha", 88), ("Ravi", 72), ("Meera", 95), ("Karan", 59), ("Divya", 81)]
total=0
top=students[0]
bottom=students[0]
for name,marks in students:
    print(name)
    print(marks)

    if marks>=90:
        print("A")
    elif marks>=80:
        print("B")
    elif marks>=70:
        print("C")
    elif marks>=60:
        print("D")
    else:
        print("F")

    total=total+marks

    if marks > top[1]:
        top = name, marks

    if bottom[1] > marks:
        bottom = name, marks

average=total/len(students)
print(average)
print(top)
print(bottom)
