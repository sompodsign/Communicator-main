import time

from pages.base_page import BasePage
from data.locators import MessagesLocator
from data.data import *


class MessagePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = MessagesLocator
        self.data = Data

    def click_new_message_btn(self):
        self.click_by_id(self.locator.new_message_btn)

    def send_number_to_field(self, number):
        self.send_data_by_id(number, self.locator.to_field)

    def send_messages(self):
        for i in ['01521239970', '01705569768']:
            self.send_message_to_a_number(i)
            time.sleep(1)
            self.driver.hide_keyboard()
            self.go_back()


    def write_message_to_field(self, message):
        self.wait_element(self.locator.message_field)
        self.send_data_by_id(message, self.locator.message_field)

    def click_send_btn(self):
        self.click_by_id(self.locator.send_button)

    def send_message_to_a_number(self, number):
        self.click_new_message_btn()
        self.send_number_to_field(number)
        self.keyboard_keycode_press(66)
        self.write_message_to_field('Test SMS')
        self.click_send_btn()


