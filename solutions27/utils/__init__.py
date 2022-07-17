from tqdm import tqdm
import shutil
from pathlib import Path

def generate_paths(problem_number):
    result = dict()
    for letter in ['A', 'B']:
        result[letter] = './data/27data/{}/27-{}{}.txt'.format(problem_number, problem_number, letter.lower())
    
    return result

def test_with_bruteforce(f_bruteforce, f, input_generator, verbose=False):
    """
    Тестирует эффективный алгоритм случайными тестами при помощи не эффективного

    ## Параметры

    `f_bruteforce`: Неэффективное переборное решение.

    `f (function)`: Эффективное решение.

    `input_generator`: Функция, генерирующая данные.
    """

    path = 'tmp.txt'
    
    failed_tests = 0
    # print('\nRunning random tests...')
    # for test_id in tqdm(range(1, 1000+1)):
    for test_id in range(1, 1000+1):
        input_generator(path)
        expected = f_bruteforce(path)
        actual = f(path)
        
        if expected != actual:
            failed_tests += 1
            test_info_path = "./tmp/{}".format(f.__module__)
            Path(test_info_path).mkdir(parents=True, exist_ok=True)
            
            if verbose:
                print('Test {} failed. Expected {}, actual {}'.format(test_id, expected, actual))
            
            shutil.copy('tmp.txt', '{}/test{}_data.txt'.format(test_info_path, test_id))
            with open('{}/test{}_info.txt'.format(test_info_path, test_id), 'w+') as test_case_info:
                test_case_info.write('Expected {}, actual {}'.format(expected, actual))

        if failed_tests >= 10:
            if verbose:
                print('Stopped random testing after 10 failed tests.')
            break

    return failed_tests == 0

