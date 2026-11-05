import re

dna = "ACTNGCATRGCTACGTYACGATSCGAWTCG"

# Split the string wherever a character is NOT A, T, G, or C
output = re.split(r'[^ATGC]', dna)

print(output)