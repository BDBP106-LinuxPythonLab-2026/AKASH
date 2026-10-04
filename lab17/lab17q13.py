L = [1, 2, 2, 3, 3, 3, 4,]
result_list = []
k = 1

for i in L:
    if L.count(i) > k and i not in result_list:
        result_list.append(i)

print(result_list)
