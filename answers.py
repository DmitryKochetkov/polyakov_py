import pandas as pd
import argparse

answers = pd.read_csv('./data/answers.csv', encoding='windows-1251')
answers.index += 1
# Первая строчка ответов на 19-21 задачи содержит какую-то ссылку на YouTube
answers.iloc[0, 0] = '17'
answers.iloc[0, 1] = '29 32'
answers.iloc[0, 2] = '28'

def get_correct_answer(problem_type: int, problem_number) -> str:
    return answers[str(problem_type)][problem_number]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('type', metavar='type', type=int, help='Problem type (1-27)')
    parser.add_argument('problem', metavar='problem', type=int, help='Problem number (min: 1, max: depends on type)')

    args = parser.parse_args()
    problem_type = args.type
    problem_number = args.problem

    print(get_correct_answer(problem_type, problem_number))