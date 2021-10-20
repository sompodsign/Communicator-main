from pages.base_page import BasePage
from data.locators import GoogleMessagesPageLocator
from data.data import *
from utils.readUserData import phoneNumber, messages
from time import sleep


class GoogleMessagesPage(BasePage):

    def __init__(self, driver):
        self.locator = GoogleMessagesPageLocator
        self.data = Data
        super().__init__(driver)

    def send_message(self):
        sleep(self.data.five_seconds)
        for i in range(len(phoneNumber)):
            self.click(self.locator.start_chat)
            self.send_data(phoneNumber[i], self.locator.to)
            self.send_data(messages[i], self.locator.message_input)
            # self.click(self.locator.sendMessage)
            self.click(self.locator.back)

    def send_group_message(self):
        sleep(self.data.five_seconds)
        for i in range(len(phoneNumber)):
            self.click(self.locator.start_chat)
            self.send_data(phoneNumber[i], self.locator.to)

        self.send_data(messages[1], self.locator.message_input)
        # self.click(self.locator.sendMessage)
        self.click(self.locator.back)
