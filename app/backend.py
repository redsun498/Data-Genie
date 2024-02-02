import pandas as pd

def load_data():
    data = pd.read_csv(r"..\..\data_files\cleaned\'all_drinks_cleaned.csv")
    return data