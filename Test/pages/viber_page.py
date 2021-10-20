from pages.base_page import BasePage
from data.locators import ViberPageLocator
from data.data import *
from time import sleep
from utils.excel_utils_pandas import *
from utils.gspread_utils import *


class ViberPage(BasePage):

    def __init__(self, driver):
        self.locator = ViberPageLocator
        self.data = Data
        self.viberdata = Whatsapp
        super().__init__(driver)

    def read_excel_for_availability(self, file, sheet):
        df = read_excel_sheet_by_sheet_name_pandas_without_header(file, sheet)
        df = df.loc[:, 0]
        phone_number = df.values.tolist()
        return phone_number

    def write_res_to_excel(self, file, sheet, data):
        df = read_excel_sheet_by_sheet_name_pandas_without_header(file, sheet)
        # df[len(df.columns)+1] = data
        df = pd.concat([df, pd.DataFrame(data)], axis=1)
        df.to_excel(excel_writer=file, sheet_name=sheet, index=False, header=None)

    def read_number_from_gspread(self, gsheet, sheet_name, column_num):
        client = get_authorized_client(json_file)
        gsheet = open_spreadsheet_by_filename(client, gsheet)
        worktsheet = select_worksheet_by_name(gsheet, sheet_name)
        phone_number = get_single_col_value(worktsheet, column_num)
        return phone_number

    def read_escaped_number_from_gspread(self, gsheet, sheet_name, column_num, value):
        client = get_authorized_client(json_file)
        gsheet = open_spreadsheet_by_filename(client, gsheet)
        worktsheet = select_worksheet_by_name(gsheet, sheet_name)
        escaped_cell = find_all_matched_cells_by_value_in_col(worktsheet, column_num, value)
        escaped_row = [i.row for i in escaped_cell]
        return escaped_row

    def write_result_on_gspread(self, gsheet, sheet_name, row, column, data):
        client = get_authorized_client(json_file)
        gsheet = open_spreadsheet_by_filename(client, gsheet)
        worksheet = select_worksheet_by_name(gsheet, sheet_name)
        update_cell(worksheet, row, column, data)

    def get_wa_available_phone_number_excel(self, file, sheet):
        df = read_excel_sheet_by_sheet_name_pandas_without_header(file, sheet)
        df = df.fillna('False')
        # df.columns = ['phone', 'availability']
        # print('\n', df)
        # print('#########################')
        # # print(list(df.columns.values))
        # df = df.loc[df['availability'] == True]
        df = df.loc[df[1] == True]
        # print('\n', df)
        # available_phone_number = df[['phone']]
        df = df.loc[:, 0]
        available_phone_number = df.values.tolist()
        # print(available_phone_number)
        return available_phone_number

    def get_wa_available_phone_number_gsheet(self, gsheet, sheet_name, phone_column_num, result_column_num, value):
        client = get_authorized_client(json_file)
        gsheet = open_spreadsheet_by_filename(client, gsheet)
        worktsheet = select_worksheet_by_name(gsheet, sheet_name)
        escaped_cell = find_all_matched_cells_by_value_in_col(worktsheet, result_column_num, value)
        phone_number = get_single_col_value(worktsheet, phone_column_num)
        available_phone_number_row = [i.row for i in escaped_cell]
        available_phone_number = [phone_number[i - 1] for i in available_phone_number_row]
        return available_phone_number

    def viber_number_finder(self):
        # phone_number = self.read_excel_for_availability(self.viberdata.file_for_availability, self.viberdata.sheet_for_availability)
        phone_number = self.read_number_from_gspread(self.viberdata.gsheet_name, self.viberdata.gsheet_worksheet, 1)
        # print(phone_number)
        result = ''
        for i in range(0, len(phone_number)):  # For initial run
            # for i in range(10275, 20000):          # For specific range
            try:
                self.click(self.locator.search)
                self.click(self.locator.search_input)
                self.send_data(f'{self.viberdata.country_code_BD}{int(phone_number[i])}', self.locator.search_input)  # For initial run
                self.driver.hide_keyboard()
                try:
                    res = self.is_element_displayed(self.locator.chat_person)
                    if res is True:
                        result = 'True'
                except Exception as e:
                    result = 'False'
                self.go_back()
                # self.write_result_on_gspread(self.viberdata.gsheet_name, self.viberdata.gsheet_worksheet, i + 1, 2, result)  # For initial run
            except:
                continue
        # writesinglecol(self.viberdata.file_for_availability, self.viberdata.sheet_for_availability, 1, 2, i + 1, result)
        # print (result)
        # self.write_res_to_excel(self.viberdata.file_for_availability, self.viberdata.sheet_for_availability, result)

    def viber_number_finder_for_escaped_number(self):
        # phone_number = self.read_excel_for_availability(self.viberdata.file_for_availability, self.viberdata.sheet_for_availability)  # local excel
        phone_number = self.read_number_from_gspread(self.viberdata.gsheet_name, self.viberdata.gsheet_worksheet, 1)
        escaped_row = self.read_escaped_number_from_gspread(self.viberdata.gsheet_name, self.viberdata.gsheet_worksheet, 2, '')
        # print(phone_number)
        # print(escaped_row)
        result = ''
        for i in range(0, len(escaped_row)):  # For escaped value
            try:
                self.click(self.locator.search)
                self.send_data(f'{self.viberdata.country_code_BD}{int(phone_number[escaped_row[i] - 1])}', self.locator.search_input)  # For escaped value
                self.driver.hide_keyboard()
                try:
                    res = self.is_element_displayed(self.locator.chat_person)
                    if res is True:
                        result = 'True'
                except Exception as e:
                    result = 'False'
                self.go_back()
                self.write_result_on_gspread(self.viberdata.gsheet_name, self.viberdata.gsheet_worksheet, escaped_row[i], 2, result)  # For escaped value
            except:
                continue
        # writesinglecol(self.viberdata.file_for_availability, self.viberdata.sheet_for_availability, 1, 2, i + 1, result) # local excel openpyxl
        # print (result)
        # self.write_res_to_excel(self.viberdata.file_for_availability, self.viberdata.sheet_for_availability, result) # local excel pandas

    def send_message_based_on_availability(self):
        # available_phone_number = self.get_wa_available_phone_number_excel(self.viberdata.file_for_availability, self.viberdata.sheet_for_availability)
        available_phone_number = self.get_wa_available_phone_number_gsheet(self.viberdata.gsheet_name, self.viberdata.gsheet_worksheet, 1, 2, 'TRUE')
        print(available_phone_number)
        print(len(available_phone_number))
        for i in range(0, len(available_phone_number)):
            self.click(self.locator.search)
            sleep(self.data.one_second)
            self.send_data(f'{self.viberdata.country_code_BD}{int(available_phone_number[i])}', self.locator.search_input)
            self.driver.hide_keyboard()
            try:
                self.click(self.locator.chat_person)
                self.send_data(self.viberdata.message, self.locator.chat_message)
                sleep(self.data.point_five)
                self.click(self.locator.post_message)
                self.go_back()
                sleep(self.data.point_five)
            except Exception as e:
                print(e)

    def send_image(self):
        available_phone_number = self.read_excel_for_availability(self.viberdata.file_for_availability, self.viberdata.sheet_for_availability)
        available_phone_number = self.get_wa_available_phone_number_gsheet(self.viberdata.gsheet_name, self.viberdata.gsheet_worksheet, 1, 2, 'TRUE')
        # available_phone_number = self.get_wa_available_phone_number(self.viberdata.file_for_availability, self.viberdata.sheet_for_availability)
        # for i in range(0, len(available_phone_number)):
        for i in range(0, 1):
            self.click(self.locator.search)
            sleep(self.data.one_second)
            self.send_data(f'{self.viberdata.country_code_BD}{int(available_phone_number[i])}', self.locator.search_input)
            self.driver.hide_keyboard()
            try:
                self.click(self.locator.chat_person)
                self.click(self.locator.attachment)
                self.click(self.locator.gallary1)
                self.click(self.locator.image_folder)
                self.click(self.locator.photo)
                self.click(self.locator.caption)
                self.driver.hide_keyboard()
                self.send_data(self.viberdata.message, self.locator.caption_text)
                self.click(self.locator.send_image_from_gallery)
                self.click(self.locator.post_message)
                self.go_back()
            except Exception as e:
                print(e)
