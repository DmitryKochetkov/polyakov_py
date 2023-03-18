def f(x, a):
    return x % 2 != 0 or x % 3 != 0 or x + a >= 100

def check(a):
    for x in range(1, 10000):
        if not f(x, a):
            return False

    return True

for a in range(1, 1000):
    if check(a):
        print(a)
        break