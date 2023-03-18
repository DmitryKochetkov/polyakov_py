from itertools import product

digits = list(range(8))
c = 0
for item in product(digits, repeat=5):
    if item[0] != 0 and item.count(6) == 1:
        p = item.index(6)
        if (((p > 0 and item[p-1] % 2 == 0) or (p == 0)) and ((p < len(item)-1 and item[p+1] % 2 == 0) or p == len(item)-1)):
            c += 1

print(c)