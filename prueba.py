from itertools import cycle
l1 = [1, 3, 5]
l2 = [1, 2, 3, 4, 5]

for e, e2 in zip(cycle(l1), l2):
    print(e, e2)
