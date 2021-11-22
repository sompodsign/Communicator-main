import sys
import numpy as np
from time import sleep
from pages.base_page import BasePage
from data.locators import MessagesLocator
from data.data import Sms
from utils.csv_utils import read_csv_without_header, write_send_status_to_csv


class MessagePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = MessagesLocator
        self.message = Sms.message
        self.mobile_numbers = None

    def click_new_message_btn(self):
        # clicks the message button on main screen
        sleep(0.1)
        self.wait_element(self.locator.new_message_btn)
        self.click_by_id(self.locator.new_message_btn)

    def send_number_to_field(self, number):
        """
        Enter mobile number to "TO" field.
        :param number:
        :return:
        """
        self.wait_element(self.locator.to_field)
        self.send_data_by_id(number, self.locator.to_field)

    def send_messages(self):
        """ Send message which is saved in
        sheet to all the mobile numbers in sheet
        """
        self.mobile_numbers = np.array(read_csv_without_header(file_name=Sms.file_path)['Mobile Numbers'])
        total_numbers = len(self.mobile_numbers)
        for i in range(total_numbers):
            number = "0{}".format(self.mobile_numbers[i])
            print("Sending message to... 0{}".format(self.mobile_numbers[i]))
            self.send_message_to_a_number(number, self.message)
            write_send_status_to_csv(Sms.file_path, 'Done', i)
            print("Processed {} / {}\n".format(i+1, total_numbers))
            self.driver.hide_keyboard()
            self.go_back()
        print("COMPLETE!!!")

    def write_message_to_field(self, message):
        """
        Writes message in the message field
        :param message:
        :return:
        """
        self.wait_element(self.locator.message_field)
        self.send_data_by_id(message, self.locator.message_field)

    def click_send_btn(self):
        self.wait_element(self.locator.send_button)
        self.click_by_id(self.locator.send_button)

    def send_message_to_a_number(self, number, message):
        """
        Sends message to a single mobile number.
        :param message:
        :param number:
        :return:
        """
        if self.current_activity() != '.home.HomeActivity':
            sys.exit()
        else:
            self.click_new_message_btn()
            self.send_number_to_field(number)
            self.keyboard_keycode_press(66)
            self.write_message_to_field(message)
            self.click_send_btn()

    def current_activity(self):
        return self.driver.current_activity
