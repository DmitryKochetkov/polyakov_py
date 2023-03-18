def f(n):
    s = ''
    d = 0
    while n > 0:
        s = s + str(n % 2)
        d += n % 2
        n //= 2
    
    if d % 2 == 0:
        s = '10' + s[2:] + '0'
    else:
        s = '11' + s[2:] + '1'
    return int(s, 2)

for i in range(1, 100):
    if f(i) >= 40:
        print(i)
        break