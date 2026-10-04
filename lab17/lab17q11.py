L=[1,2,3,4,4,5,6,7,5,8,9,6]


for i in range (1,len(L)):

    for j in range (i+1,len(L)):
          if L[i]==L[j] :
              print("Number are:",L[j] )
