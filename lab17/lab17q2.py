# def base_power(B , n):
#     result = B**n
#     print(result)
#
# base_power(2, 5)

#using for loop for the same problem

B= int(input("Enter the number: "))
n= int(input("Enter the number: "))

result =1
for i in range(n+1):
    result *= i
    print(result)
