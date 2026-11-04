#Program to create dictionary
#Program to create dictionary with odd numbers
#from 1 to 20 , with values as their cubes
n=20
odd_dict=dict([])
for i in range(1,n+1):
    if i%2!=0:
        odd_dict[i]=i**3
print(odd_dict)