from pages.base_page import BasePage
from data.locators import GChatPageLocator
from data.data import *
from utils.readUserData import email, message, seenOldBound, room
from utils.excel_utils import *
from time import sleep
import re


class GChatPage(BasePage):

    def __init__(self, driver):
        self.locator = GChatPageLocator
        self.data = Data
        super().__init__(driver)

    def send_message(self):
        sleep(self.data.five_seconds)
        # self.click(self.locator.ok)
        # # only for rk device
        # self.click(self.locator.changeProfile)
        # self.click(self.locator.shQups)
        # res = self.is_element_displayed(self.locator.ok)
        # if res is True:
        #     self.click(self.locator.ok)
        # self.click(self.locator.searchbutton)
        self.click(self.locator.new_chat)
        seenBound = []
        for i in range(len(email)):
            self.send_data(email[i], self.locator.search_text)
            self.click(self.locator.select_person)
            res = self.is_element_displayed(self.locator.seen_message)
            if res is True:
                val = self.get_attribute_value(self.data.bounds_attribute, self.locator.seen_message)
                val = re.findall(r'[-\d]+', val)
                seenBound.append(val)
            self.send_data(message[i], self.locator.chat_message)
            self.click(self.locator.post_message)
            self.go_back()
            self.click(self.locator.new_chat)
        writesinglecol(user_data, gchat, len(seenBound), 4, 1, seenBound)

    def seen_message(self):
        sleep(self.data.five_seconds)
        # self.click(self.locator.ok)
        # self.click(self.locator.changeProfile)
        # self.click(self.locator.shQups)
        # res = self.is_element_displayed(self.locator.ok)
        # if res is True:
        #     self.click(self.locator.ok)
        # self.click(self.locator.searchbutton)
        self.click(self.locator.new_chat)
        seenNewBound = []
        for i in range(len(email)):
            self.send_data(email[i], self.locator.search_text)
            self.click(self.locator.select_person)
            res = self.is_element_displayed(self.locator.seen_message)
            if res is True:
                val = self.get_attribute_value(self.data.bounds_attribute, self.locator.seen_message)
                val = re.findall(r'[-\d]+', val)
                seenNewBound.append(val)
                print(val)
            else:
                seenNewBound.append(seenOldBound[i])
            self.go_back()
            self.click(self.locator.new_chat)

        result = []
        for i in range(len(seenOldBound)):
            res = False
            for j in range(4):
                if int(seenOldBound[i][j]) < int(seenNewBound[i][j]):
                    res = True
                    break
            if res is True:
                result.append('Seen')
            else:
                result.append('Not seen')

        writesinglecol(user_data, gchat, len(result), 3, 1, result)

    def post_room_message(self):
        # self.click(self.locator.ok)
        self.click(self.locator.rooms)
        sleep(1)
        self.click(self.locator.search_btn)

        for i in range(len(room)):
            self.send_data(room[i], self.locator.search_text1)
            self.click(self.locator.searched_room)
            self.send_data(message[i], self.locator.chat_message)
            self.click(self.locator.post_message)
            self.go_back()
