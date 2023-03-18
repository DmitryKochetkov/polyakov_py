a = []
with open('./data/18data/18-77.txt') as f:
    for line in f.readlines():
        a.append(float(line))

s = a[0]
m = 0
for i in range(1, len(a)):
    

print(max(m))
