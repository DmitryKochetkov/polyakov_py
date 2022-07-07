# Сопоставление номеров задач и путей к входным файлам

problem24_files = { 
    1: './data/24data/k7data/k7-0.txt',
    2: './data/24data/k7data/k7-3.txt',
    3: './data/24data/k7data/k7-5.txt',
    4: './data/24data/k7data/k7-20.txt',
    5: './data/24data/k7data/k7-25.txt',
    6: './data/24data/k7data/k7-29.txt',
    7: './data/24data/k7data/k7-40.txt',
    8: './data/24data/k7data/k7-42.txt',
    9: './data/24data/k7data/k7-44.txt',
    10: './data/24data/k7data/k7-45.txt',
    11: './data/24data/k7data/k7-53.txt',
    12: './data/24data/k7data/k7-70.txt',
    13: './data/24data/k7data/k7-75.txt',
    14: './data/24data/k7data/k7-80.txt',
    15: './data/24data/k7data/k7-84.txt',
    16: './data/24data/k7data/k7-91.txt',
    17: './data/24data/k7data/k7-94.txt',
    18: './data/24data/k7data/k7-96.txt',
    19: './data/24data/k7data/k7-97.txt',
    20: './data/24data/k7data/k7-100.txt',
    26: './data/24data/k7data/k7a-6.txt',
    77: './data/24data/k8data/k8-1.txt',
    78: './data/24data/k8data/k8-2.txt',
    79: './data/24data/k8data/k8-3.txt',
    80: './data/24data/k8data/k8-4.txt',
    81: './data/24data/k8data/k8-5.txt',
    82: './data/24data/k8data/k8-6.txt',
    83: './data/24data/k8data/k8-7.txt',
    84: './data/24data/k8data/k8-8.txt',
    85: './data/24data/k8data/k8-9.txt',
    86: './data/24data/k8data/k8-10.txt',
    87: './data/24data/24-1.txt'
}

def get_file_path(problem_number: int):
    assert problem_number in problem24_files, 'Некорректный номер задачи типа 24'
    return problem24_files[problem_number]