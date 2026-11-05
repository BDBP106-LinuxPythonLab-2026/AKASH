import numpy as np

#i)
# import numpy as np
#
# arr = np.arange(10)
#
# print(arr)

#II)
arr = np.zeros((3, 3), dtype=bool)

print(arr)


#iii)
# (4) Thinking along the same lines of the above question, how will you swap two columns in
# a 2D array? Define a 3x3 matrix with random values, and swap first and second columns
# in this array.
arr = np.arange(1, 51)

prime = arr[
    np.array([all(n % i != 0 for i in range(2, int(n**0.5) + 1))
              and n > 1 for n in arr])
]

print(prime)


#iv
arr = np.random.randint(1, 100, 20)

print("1D Array:")
print(arr)

arr2 = arr.reshape(4, 5)

print("4x5 Array:")
print(arr2)


#v)
a = np.arange(10)
b = np.ones(10, dtype=int)

result = np.hstack((a, b))

print("Array a:", a)
print("Array b:", b)
print("Stacked Array:", result)

#vii)
result = np.setdiff1d(a, b)

print("Elements in a but not in b:")
print(result)

#viii
a = np.arange(1, 101)
b = np.array([2, 3, 5, 7, 11, 13, 17, 19])

indices = np.where(np.isin(a, b))

print("Indices of common elements:")
print(indices)


#ix
a = np.arange(1, 101)

result = a[(a > 5) & (a < 20)]

print(result)
