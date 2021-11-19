import pandas as pd


def read_csv_without_header(file_name):
    dataframe = pd.read_csv(file_name)
    return dataframe


def write_send_status_to_csv(file, data, row):
    df = read_csv_without_header(file)
    df.iloc[row, 1] = data
    df.to_csv(file, index=False)