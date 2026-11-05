import numpy as np

sequence = "GATTACA"

# Mapping of DNA bases
mapping = {
    'A': [1, 0, 0, 0],
    'C': [0, 1, 0, 0],
    'G': [0, 0, 1, 0],
    'T': [0, 0, 0, 1]
}

# Convert DNA sequence into one-hot encoding
encoded = np.array([mapping[base] for base in sequence])

print("DNA Sequence:", sequence)
print("One-Hot Encoding:")
print(encoded)
