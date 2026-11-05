import re

# DNA sequence and regex pattern using character groups
dna = "ATCGCGAATTGCAC"
pattern = r"GC[ATGC]GC"

# Search for the restriction site
if re.search(pattern, dna):
    print("Restriction site found!")
else:
    print("Restriction site not found.")