import unittest
from answers import get_correct_answer
from functools import lru_cache

def moves(t):
    a, b = t
    return [(a+2, b), (a, b+2), (a*2, b), (a, b*2)]

def win_condition(t):
    return sum(t) >= 231

@lru_cache(None)
def game19(t):
    if win_condition(t):
        return 'W'
    
    if any([game19(move) == 'W' for move in moves(t)]):
        return 'P1'

    if any([game19(move) == 'P1' for move in moves(t)]):
        return 'V1'

@lru_cache(None)
def game20_21(t):
    if win_condition(t):
        return 'W'
    
    if any([game20_21(move) == 'W' for move in moves(t)]):
        return 'P1'

    if all([game20_21(move) == 'P1' for move in moves(t)]):
        return 'V1'
    
    if any([game20_21(move) == 'V1' for move in moves(t)]):
        return 'P2'

    if all([game20_21(move) in ['P1', 'P2'] for move in moves(t)]):
        return 'V2'

def solve():
    answer = {}
    v1 = []
    p2 = []
    v2 = []

    for s in range(1, 232):
        initial_state = (17, s)
        winner = game19(initial_state)
        if winner == 'V1':
            v1.append(s)

    for s in range(1, 232):
        initial_state = (17, s)
        winner = game20_21(initial_state)
        if winner == 'P2':
            p2.append(s)
        elif winner == 'V2':
            v2.append(s)

    answer[19] = max(v1)
    answer[20] = f'{min(p2)} {max(p2)}'
    answer[21] = min(v2)

    return answer

if __name__ == '__main__':
    answer = solve()
    print('19:', answer[19])
    print('20:', answer[20])
    print('21:', answer[21])

class Problem109(unittest.TestCase):
    def test(self):
        answer = solve()

        assert str(answer[19]) == get_correct_answer(19, 109)
        assert str(answer[20]) == get_correct_answer(20, 109)
        assert ' '.join([str(i) for i in answer[21]]) == get_correct_answer(21, 109)
