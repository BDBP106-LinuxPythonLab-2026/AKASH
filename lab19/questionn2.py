a = [x for x in range(1, 51)]
# #i)
# total = 0
# for x in a:
#     total += x
# print(total)
#
#ii)
b=[]

for x in a:
    if x %2!=0:
        b.append(x)
print(b)

#

#(iii) Using a do loop structure, collect all the common numbers in a and b into a new list c.

c=[]
for i in a:
    if i in b :
        c.append(i)
print(c)


