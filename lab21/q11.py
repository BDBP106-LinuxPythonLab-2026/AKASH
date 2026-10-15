from functools import reduce

words = ["Python", "is", "easy"]

result = reduce(lambda x, y: x + ' ' + y, words)

print(result)
