import pandas as pd


def read_excel_pandas(file_name):
    dataframe = pd.read_excel(file_name)
    return dataframe


def read_excel_sheet_by_index_pandas(file_name, index):
    dataframe = pd.read_excel(file_name, sheet_name=index)
    return dataframe


def read_excel_sheet_by_sheet_name_pandas(file_name, sheet_name):
    dataframe = pd.read_excel(file_name, sheet_name=sheet_name)
    return dataframe


def read_excel_sheet_by_sheet_name_pandas_without_header(file_name, sheet_name):
    dataframe = pd.read_excel(file_name, sheet_name=sheet_name, header=None, )
    return dataframe


def read_sheet_pandas(sheet_name):
    dataframe = pd.DataFrame(sheet_name.get_all_rocords())
    return dataframe


def get_df_info(dataframe):
    return dataframe.info()


def get_max_row(dataframe):
    return len(dataframe)


def get_max_column(dataframe):
    return len(dataframe.columns)


def get_max_row_column(dataframe):
    return dataframe.shape


def get_number_of_elements(dataframe):
    return dataframe.size


def xlsx_to_csv(excel_file, excel_sheet, csv_file):
    df = pd.read_excel(excel_file, excel_sheet, dtype=str, index_col=None, header=None)
    df.to_csv(csv_file, encoding='utf-8', index=None, header=None)

# def write_res_to_excel(file, sheet, data, starting_column):
#     df = pd.DataFrame(data)
#     df.to_excel(excel_writer=file, sheet_name=sheet, startrow = 2, startcol=starting_column, index=False, header=None)
#
# def write_res_to_excel(file, sheet, data, starting_column):
#     df = pd.DataFrame(data)
#     df.to_excel(excel_writer=file, sheet_name=sheet, startcol=starting_column, index=False, header=None)

# def write_res_to_excel(file, sheet, data):
#     df = read_excel_sheet_by_sheet_name_pandas_without_header(file, sheet)
#     # df[len(df.columns)+1] = data
#     ddf = pd.concat([df, pd.DataFrame(data)], axis=1)
#     ddf.to_excel(excel_writer=file, sheet_name=sheet, index=False, header=None)

# def write(file, sheet, data):
#     df = pd.DataFrame(data)
#     with pd.ExcelWriter(file, engine='openpyxl', mode='a') as writer:
#         df.to_excel(writer, sheet_name=sheet, startcol=2, index=False, header=None)
#         writer.save()
#     writer.close()
#