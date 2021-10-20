from pages.base_page import BasePage
from data.locators import ImoPageLocator
from data.data import *
from time import sleep
from utils.excel_utils_pandas import *
from utils.gspread_utils import *


class ImoPage(BasePage):

    def __init__(self, driver):
        self.locator = ImoPageLocator
        self.data = Data
        self.imodata = Imo
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

    def write_result_on_gspread(self, gsheet, sheet_name, row, column, data):
        client = get_authorized_client(json_file)
        gsheet = open_spreadsheet_by_filename(client, gsheet)
        worktsheet = select_worksheet_by_name(gsheet, sheet_name)
        update_cell(worktsheet, row, column, data)

    def get_imo_available_phone_number(self, file, sheet):
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

    def imo_number_finder(self):
        phone_number = self.read_number_from_gspread(self.imodata.gsheet_name, self.imodata.gsheet_worksheet, 1)
        result = ''
        # for i in range(0, len(phone_number)):
        for i in range(431, 2000):
            try:
                self.click(self.locator.search)
                sleep(self.data.point_five)
                self.send_data(f'{self.imodata.country_code_BD}{int(phone_number[i])}', self.locator.search_input)
                self.driver.hide_keyboard()
                try:
                    res = self.is_element_displayed(self.locator.chat_person)
                    if res is True:
                        result = 'True'
                except Exception as e:
                    result = 'False'
                self.go_back()
                self.write_result_on_gspread(self.imodata.gsheet_name, self.imodata.gsheet_worksheet, i + 1, 3, result)
            except:
                continue

    def send_message_based_on_availability(self):
        available_phone_number = ['01682233357']
        available_phone_number = self.get_imo_available_phone_number(self.wdata.file_for_availability, self.wdata.sheet_for_availability)
        for i in range(0, len(available_phone_number)):
            self.click(self.locator.search)
            sleep(self.data.point_five)
            self.send_data(f'0{int(available_phone_number[i])}', self.locator.search_input)
            self.driver.hide_keyboard()
            try:
                self.click(self.locator.chat_person)
                self.send_data(self.imodata.message, self.locator.chat_message)
                sleep(self.data.point_five)
                self.click(self.locator.post_message)
                sleep(self.data.point_five)
                self.go_back()
            except Exception as e:
                print(e)

    def send_image(self):
        available_phone_number = self.read_excel_for_availability(self.imodata.file_for_availability,self.imodata.sheet_for_availability)
        # available_phone_number = self.get_wa_available_phone_number(self.wdata.file_for_availability, self.wdata.sheet_for_availability)
        # for i in range(0, len(available_phone_number)):
        for i in range(0, 1):
            self.click(self.locator.search)
            sleep(self.data.point_five)
            self.send_data(f'{self.imo.country_code_BD}{int(available_phone_number[i])}', self.locator.search_input)
            self.driver.hide_keyboard()
            try:
                self.click(self.locator.chat_person)
                self.click(self.locator.img_attachment)
                self.click(self.locator.gallary1)
                self.click(self.locator.image_folder)
                self.click(self.locator.photo)
                self.click(self.locator.caption)
                # self.driver.hide_keyboard()
                self.send_data(self.wdata.message, self.locator.caption_text)
                self.click(self.locator.send_image_from_gallery)
                # self.click(self.locator.post_message)
                self.go_back()
            except Exception as e:
                print(e)


