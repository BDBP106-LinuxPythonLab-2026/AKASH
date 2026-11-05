import numpy as np

scores = np.array([10, 25, 30, 15, 40, 50, 18, 22, 35, 12])

print("Average:", np.mean(scores))
print("Highest score:", np.max(scores))
print("Lowest score:", np.min(scores))

print("Numbers above 20:", np.sum(scores > 20))

print("Scores below 20:")
print(scores[scores < 20])
