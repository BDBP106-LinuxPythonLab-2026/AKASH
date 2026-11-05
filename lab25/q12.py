import re

dna = "ATCGCGYAATTCAC"

# Check if the sequence contains any base other than A, T, G, or C
if re.search(r"[^ATGC]", dna):
    print("The sequence contains ambiguous bases.")

    # Filter and join only the non-ambiguous bases
    non_ambiguous = "".join(re.findall(r"[ATGC]", dna))
    print(f"Non-ambiguous bases: {non_ambiguous}")
else:
    print("The sequence contains no ambiguous bases.")