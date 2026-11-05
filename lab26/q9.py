import numpy as np


counts = np.array([100, 200, 300, 400, 500])


log_values = np.round(np.log2(counts), 2)


percentage = np.round((counts / np.sum(counts)) * 100, 1)

print("Gene Counts:")
print(counts)

print("Log2 Values:")
print(log_values)

print("Percentage of Total:")
print(percentage)
