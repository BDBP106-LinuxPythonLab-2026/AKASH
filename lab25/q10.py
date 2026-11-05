# import re
#
# # Define the sequence and regular expression pattern
# dna = "ATCGCGAATTCAC"
# pattern = r"G(A|T)C"  # Alternatively, r"GG[AT]CC" can also be used
#
# # Check for a match
# if re.search(pattern, dna):
#     print("AvaII restriction site found!")
#     print("GGACC or GGTCC")
# else:
#     print("AvaII restriction site not found.")

import re

# Example DNA containing the 'GGTCC' variant
dna = "ATCGCGAATTGGTCCTCAC"
pattern = r"GG[AT]CC"

match = re.search(pattern, dna)

if match:
    # match.group() returns the exact string that matched the pattern
    print(match.group())
else:
    print("No AvaII restriction site found.")