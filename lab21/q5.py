from functools import reduce
numbers = [5, 15, 45, 135 ]
result = reduce(lambda a, b: a + b, numbers)

print("Sum of all elements:", result)

