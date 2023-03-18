a = list()
m3 = -10001 # максимальный, оканчивающийся на 3

with open('./17.txt') as f:
    for line in f.readlines():
        x = int(line)
        a.append(x)
        if abs(x) % 10 == 3:
            m3 = max(m3, x)

c = 0
m = 0

for i in range(len(a)-1):
    j = i+1
    s = a[i] ** 2 + a[j] ** 2
    if (((abs(a[i]) % 10 == 3) and (abs(a[j]) % 10 != 3)) or ((abs(a[i]) % 10 != 3) and (abs(a[j]) % 10 == 3))) and (s >= m3 ** 2):
        c += 1
        m = max(m, s)

print(c, m)