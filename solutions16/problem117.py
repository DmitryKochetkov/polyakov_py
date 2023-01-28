import unittest
from answers import get_correct_answer
from tqdm import tqdm
from functools import lru_cache

@lru_cache(None) # Все равно не сработает для больших n, но для сравнительно маленьких работает быстрее
def F(n):
    if n == 0:
        return 1
    if n % 2 == 1:
        return 1 + F(n-1)
    return F(n // 2)

# F(x) = 3 для всех x = 3 * 2^n и для всех x: F(x-1) = 2
# F(x-1) = 2 <=> x-1 - степень двойки

def is_power2(x):
    while x > 0 and x % 2 == 0:
        x //= 2
    return x == 1

def F_equals3(n):
    if n == 0:
        return False
    
    if n % 3 == 0 and is_power2(n // 3):
        return True

    if n % 5 == 0 and is_power2(n // 5):
        return True

    if n-1 > 1 and is_power2(n-1):
        return True
    
    return False

def solve():
    c = 0
    for n in tqdm(range(1, 500000001)):
        if F(n) == 3:
            c += 1
    return c

class Problem117(unittest.TestCase):
    def test(self):
        for n in range(100):
            assert (F(n) == 3) == F_equals3(n), f'F({n}) = {F(n)}, but F_equals3({n}) is {F_equals3(n)}'
        # assert str(solve()) == get_correct_answer(16, 117)

if __name__ == '__main__':
    for n in range(50):
        print(f'F({n}) = {F(n)}')
    
    # print(solve())