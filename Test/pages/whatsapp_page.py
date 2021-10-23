from pages.base_page import BasePage
from data.locators import WhatsappPageLocator
from data.data import *
from utils.readUserData import *
from time import sleep


class WhatsAppPage(BasePage):

    def __init__(self, driver):
        self.locator = WhatsappPageLocator
        self.data = Data
        super().__init__(driver)

    def send_message(self):
        sleep(self.data.five_seconds)
        not_send = []
        for i in range(len(phone)):
            self.click(self.locator.search)
            self.send_data(phone[i], self.locator.search_input)
            self.driver.hide_keyboard()
            try:
                self.click(self.locator.chat_person)
                sleep(1)
                self.send_data("An automated message from COMMUNICATOR.......", self.locator.chat_message)
                # sleep(1)
                self.click(self.locator.post_message)
                print(i)
                self.go_back()
            except Exception as e:
                a = e
                print('>>>>>>>', i)
                self.go_back()
                not_send.append(i)
        print(not_send)

    # def send_group_message(self):
    #     sleep(self.data.five_seconds)
    #     for i in range(len(whatsAppGroup)):
    #         self.click(self.locator.search)
    #         self.send_data(whatsAppGroup[i], self.locator.search_input)
    #         self.driver.hide_keyboard()
    #         self.click(self.locator.chat_person)
    #         self.send_data(whatsAppGroupMessage[i], self.locator.chat_message)
    #         self.click(self.locator.post_message)
    #         self.go_back()

    # def extract_group_contact(self):
    #     sleep(self.data.five_seconds)
    #     self.click(self.locator.search)
    #     self.send_data(self.data.group_name, self.locator.search_input)
    #     self.driver.hide_keyboard()
    #     # self.click(self.locator.chat_person)
    #     # self.click(self.locator.more_options)
    #     # self.click(self.locator.group_info)
    #     self.click(self.locator.group_info_direct)
    #
    #     val = self.get_attribute_value(self.data.text_attribute, self.locator.total_members)
    #     total_members = val.split(' ')[0]
    #     print(total_members)

        # size = self.driver.get_window_size()
        # print(size)
        # x = size['width']
        # y = size['height']
        #
        # def swipe_down():
        #     x1 = x * 0.5
        #     y1 = y * 0.1
        #     y2 = y * 0.9
        #     t = 1000
        #     n = 3  # n indicates the number of swipes
        #     sleep(1)
        #     for i in range(n):
        #         self.driver.swipe(x1, y1, x1, y2, t)
        # swipe_down()
        # self.driver.execute_script("mobile: scroll", {'direction': 'down'})

