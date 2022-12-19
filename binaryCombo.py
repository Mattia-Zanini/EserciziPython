import itertools
n = 5
lst = list(map(list, itertools.product([0, 1], repeat=n)))

for i in range(0, len(lst)):
    print(str(i) + ") " + str(lst[i]))