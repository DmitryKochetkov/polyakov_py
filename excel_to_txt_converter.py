import pandas as pd
import os

excel_folder_names = ['22data']

for folder in excel_folder_names:
    for file in os.listdir(f'./data/{folder}'):
        file_name, extension = os.path.splitext(f'./data/{folder}/{file}')
        if extension.startswith('.xls'):
            pd.read_excel(f'./data/{folder}/{file}').to_csv(f'{file_name}.csv', encoding='utf-8', index=False, index_label=False)