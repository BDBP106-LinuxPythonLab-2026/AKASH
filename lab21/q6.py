# (6) Write a function called cell_metabolism that takes the number of glucose and oxy-
# gen molcules, that contains an inner function energy_output() to calculate ATP yield
#
# (assume 1 glucose+6 oxygen gives 38 ATP). The function should return the total ATP
# produced.

def cell_metabolism(G,O):
    if O==6*G:
        ATP=38*G
    elif G>(O/6):
        ATP=38*(O/6)
    elif G<(O/6):
        ATP=38*G
    return ATP
print(cell_metabolism(5,5))

