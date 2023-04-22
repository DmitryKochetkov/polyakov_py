from functools import lru_cache

def moves(x):
    return [x+1, 2*x]

@lru_cache(None)
def game(s):
    if s >= 129:
        return 'W'

    if any(game(m) == 'W' for m in moves(s)):
        return 'P1'

    if all(game(m) == 'P1' for m in moves(s)):
        return 'V1'

for i in range(1, 129):
    print(f'{i}: {game(i)}')
