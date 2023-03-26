def divs(a):
    d = []
    i = 2
    while i * i <= a:
        if a % i == 0:
            d.append(i)
            if i * i != a:
                d.append(a // i)
        i += 1
    return d

def check_odd_digits(x):
    return all([int(digit) % 2 != 0 for digit in str(x)])

def special_divs(a):
    return list(filter(check_odd_digits, divs(a)))

def d(a):
    spec = sorted(special_divs(a), reverse=True)
    if len(spec) < 5:
        return 0
    return spec[4]

c = 0
for n in range(300000000-1, 0, -1):
    if d(n) > 0:
        print(d(n), len(special_divs(n)))
        c += 1
    if c >= 5:
        break