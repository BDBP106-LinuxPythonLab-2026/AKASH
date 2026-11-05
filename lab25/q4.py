import re

pattern = r'^([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$'

test_values = ["000", "005", "25", "abc", "0245", "255", "0", "10"]

for value in test_values:
    if re.fullmatch(pattern, value):
        print(value, "is valid")
    else:
        print(value, "is not valid")