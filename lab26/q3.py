import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Reverse rows
print("Reverse rows:")
print(arr[::-1, :])

# Reverse columns
print("Reverse columns:")
print(arr[:, ::-1])
