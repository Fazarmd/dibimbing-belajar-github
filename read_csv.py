import pandas as pd

def read_csv_file(file_path):
    df = pd.read_csv(file_path)
    print(df)

file_path = 'username.csv'

read_csv_file(file_path)