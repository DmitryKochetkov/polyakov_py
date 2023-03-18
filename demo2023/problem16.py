def f(n):
    if n == 1:
        return 1

    return f(n-1) * n

def factorial(n):
    p = 1
    for i in range(2, n+1):
        p *= i
    return p

for i in range(1, 500):
    assert f(i) == factorial(i)

print(int(factorial(2023) / factorial(2020)))