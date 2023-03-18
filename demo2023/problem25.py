n = 10 ** 7
while n % 2023 > 0:
    n += 1

for i in range(n, 10 ** 10, 2023):
    s = str(i)
    if s[0] == '1' and s[2:6] == '2139' and s[-1] == '4' and i % 2023 == 0:
        print(i, i // 2023)
