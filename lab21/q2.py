celsius = [0, 10, 20, 100]

result = list(map(lambda c: (c * 9/5) + 32, celsius))

print(result)
print(type(result))