import pandas as pd

answers27 = pd.read_csv('answers.csv')['27'].to_list()
answers27 = [None] + answers27