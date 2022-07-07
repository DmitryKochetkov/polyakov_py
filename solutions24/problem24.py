# import unittest
# from answers import get_correct_answer
# from .utils import get_file_path

# def solution24(s):
#     answer = 0
#     a = 0

#     for i in range(len(s)):    
#         if s[i] != 'D':
#             a += 1
#         else:
#             answer = max(answer, a)
#             a = 0

#     answer = max(answer, a)

#     return answer

# with open('./data/24data/k7data/k7a-4.txt') as f:
#     s = f.readlines()[0]
#     solutions[24] = solution24(s)

# class Problems1_20(unittest.TestCase):
#     def test(self):
#         for i in range(1, 21):
#             with open(get_file_path(i)) as f:
#                 assert solve(f.read()) == get_correct_answer(24, i)

# if __name__ == '__main__':
#     print(solve())