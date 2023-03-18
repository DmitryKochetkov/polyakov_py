def f(s):
    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '22>')
        if '>2' in s:
            s = s.replace('>2', '2>')
        if '>0' in s:
            s = s.replace('>0', '1>')

    return s

def sum_digits(s):
    result = 0
    for c in s:
        if c.isdigit():
            result += int(c)
    return result

def is_prime(x):
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1

    return True

n = 0
while True:
    s = ">" + "0" * 39 + "1" * n + "2" * 39
    result = f(s)
    if is_prime(sum_digits(result)):
        print(n)
        break
    n += 1