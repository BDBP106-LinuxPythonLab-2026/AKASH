celsius = [0, 10, 20, 100]
def convert(c):
    f =(c*9/5)+32
    return f

result=(list(map(convert,celsius)))#to call a function use parenthesis
#list me convert karna padega nahi ? warna output kaise dekhoge tum log bro
print(result)
print(type(result))
