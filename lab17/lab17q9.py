S1 = "listen"
S2 = "silent"

S1_sort=sorted(S1)
S2_sort=sorted(S2)

if S1_sort == S2_sort:
       print( S1, "and" ,S2, "are ANAGRAMS")
else:
    print("are NOT anagrams")