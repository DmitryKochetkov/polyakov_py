from tqdm import tqdm

def generate_paths(problem_number):
    result = dict()
    for letter in ['A', 'B']:
        # result[letter] = '../data/27data/{}/27-{}{}.txt'.format(problem_number, problem_number, letter)
        result[letter] = 'data/27data/{}/27-{}{}.txt'.format(problem_number, problem_number, letter)
    
    return result

def test_with_bruteforce(f_bruteforce, f, input_generator, verbose=False):
    """
    Тестирует эффектвный алгоритм случайными тестами при помощи не эффективного

    ## Параметры

    `f_bruteforce`: Неэффективное переборное решение.

    `f (function)`: Эффективное решение.

    `input_generator`: Функция, генерирующая данные.
    """

    path = 'tmp.txt'
    
    failed_tests = 0
    print('\nRunning random tests...')
    for test_id in tqdm(range(1, 1000+1)):
        input_generator(path)
        expected = f_bruteforce(path)
        actual = f(path)
        
        if expected != actual:
            failed_tests += 1
            # print('Test {} failed. Expected {}, actual {}'.format(test_id, expected, actual))

        if failed_tests >= 10:
            # print('Testing is stopped after 10 failed tests.')
            break
    
    return failed_tests == 0

