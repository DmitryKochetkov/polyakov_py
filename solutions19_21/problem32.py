import unittest
from answers import get_correct_answer
from functools import lru_cache

def moves(t):
    a, b = t
    return [(a+1, b), (a, b+1), (a*2, b), (a, b*2)]

@lru_cache(None)
def game19(t):
    a, b = t
    if a + b >= 40:
        return 'W'
    
    if any([game19(move) == 'W' for move in moves(t)]):
        return 'P1'

    if any([game19(move) == 'P1' for move in moves(t)]):
        return 'V1'

@lru_cache(None)
def game20_21(t):
    a, b = t
    if a + b >= 40:
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
    answer = {
        19: 31,
        20: [],
        21: [],
    }

    for s in range(1, 31):
        initial_state = (9, s)
        winner = game19(initial_state)
        if winner == 'V1':
            answer[19] = min(answer[19], s)

    for s in range(1, 31):
        initial_state = (7, s)
        winner = game20_21(initial_state)
        if winner == 'P2':
            answer[20] = min(answer[20], s)
        elif winner == 'V2':
            answer[21].append(s)

    return answer

if __name__ == '__main__':
    answer = solve()
    print('19:', answer[19])
    print('20:', answer[20])
    print('21:', answer[21])

class Problem32(unittest.TestCase):
    def test(self):
        answer = solve()

        assert str(answer[19]) == get_correct_answer(19, 32)
        assert str(answer[20]) == get_correct_answer(20, 32)
        assert ' '.join([str(i) for i in answer[21]]) == get_correct_answer(21, 32)

if __name__ == '__main__':
    print(solve())