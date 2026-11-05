import re

dna = "ATCGCGAATTCAC"
pattern = r"GAATTC"

match = re.search(pattern, dna)
if match:
    print(match.group())
else:
    print(dna)
