import time
import numpy as np
from pages.base_page import BasePage
from data.locators import MessagesLocator
from data.data import Sms
from utils.csv_utils import read_csv_without_header, write_send_status_to_csv


class MessagePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = MessagesLocator
        self.mobile_numbers = None

    def click_new_message_btn(self):
        self.click_by_id(self.locator.new_message_btn)

    def send_number_to_field(self, number):
        self.wait_element(self.locator.to_field)
        self.send_data_by_id(number, self.locator.to_field)

    def send_messages(self):
        self.mobile_numbers = np.array(read_csv_without_header(file_name=Sms.file_path)['Mobile Numbers'])
        total_numbers = len(self.mobile_numbers)
        remaining_numbers = len(self.mobile_numbers)
        for i in range(total_numbers):
            number = "0{}".format(self.mobile_numbers[i])
            print("Sending message to {}".format(self.mobile_numbers[i]))
            self.send_message_to_a_number(number)
            write_send_status_to_csv(Sms.file_path, 'Done', i)
            print("Total sent {} / {}".format(i+1, total_numbers))
            self.driver.hide_keyboard()
            self.go_back()
            remaining_numbers -= 1
        print("Sent message to all mobile numbers.")

    def write_message_to_field(self, message):
        self.wait_element(self.locator.message_field)
        self.send_data_by_id(message, self.locator.message_field)

    def click_send_btn(self):
        self.wait_element(self.locator.send_button)
        self.click_by_id(self.locator.send_button)

    def send_message_to_a_number(self, number):
        self.click_new_message_btn()
        self.send_number_to_field(number)
        self.keyboard_keycode_press(66)
        self.write_message_to_field(Sms.message)
        self.click_send_btn()

    def current_activity(self):
        print(self.driver.current_activity)
        return self.driver.current_activity
