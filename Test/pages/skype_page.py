from pages.base_page import BasePage
from data.locators import SkypePageLocator
from data.data import *
from utils.readUserData import people, skypeName, skypeGroup, skypeMessage
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException, WebDriverException


class SkypePage(BasePage):

    def __init__(self, driver):
        self.locator = SkypePageLocator
        self.data = Data
        super().__init__(driver)

    def send_message(self):
        sleep(self.data.five_seconds)
        for i in range(len(people)):
            self.click(self.locator.search)
            self.send_data(skypeName[i], self.locator.search_input)
            self.click(self.locator.select_chat_person(people[i]))
            self.send_data(skypeMessage[i], self.locator.chat_message)
            self.click(self.locator.post_message)
            self.click(self.locator.back_from_chat)

    def send_group_message(self):
        sleep(self.data.five_seconds)
        for i in range(len(skypeGroup)):
            self.click(self.locator.search)
            self.send_data(skypeGroup[i], self.locator.search_input)
            self.click(self.locator.select_chat_person(skypeGroup[i]))
            self.send_data(skypeMessage[i], self.locator.chat_message)
            self.click(self.locator.post_message)
            self.click(self.locator.back_from_chat)

    # def extract_group_contact(self):
    #     sleep(self.data.five_seconds)
    #     profile_name = []
    #     skype_name = []
    #     self.click(self.locator.search)
    #     self.send_data(self.data.group_name, self.locator.search_input)
    #     sleep(1)
    #     self.driver.hide_keyboard()
    #     self.click(self.locator.select_chat_person(self.data.group_name))
    #     self.click(self.locator.select_chat_person(self.data.group_name))
    #     sleep(2)
    #     # sleep(8)
    #     # total_members = self.get_attribute_value(self.data.content_desc_attribute, self.locator.total_members)
    #     # total_members = total_members.split(' ')[0]
    #     # print(total_members)
    #     # TouchAction(self.driver).press(x=1077, y=2083).move_to(x=1074, y=1403).release().perform()
    #     # self.click(self.locator.show_more)
    #     #
    #
    #     # actions = TouchAction(self.driver)
    #     # actions.long_press(None, 1077, 2083)
    #     # actions.move_to(None, 1074, 1403)
    #     # actions.perform()
    #
    #     # self.driver.swipe(540, 1500, 540, 590, 1000)
    #     # self.driver.swipe(540, 1500, 540, 450, 1000)
    #
    #     ele1 = self.driver.find_element_by_xpath(self.locator.share_link_to_join)
    #     ele2 = self.driver.find_element_by_xpath(self.locator.elele)
    #     self.driver.scroll(ele2, ele1)
    #
    #     action = TouchAction(self.driver)
    #     # action.press(ele2).move_to(x=10, y=1800).release().perform()
    #     # action.press(x=1077, y=2083).move_to(x=1074, y=1403).release().perform()
    #     # action.long_press(x=1077, y=2003).move_to(x=1074, y=1403).release().perform()
    #     action.long_press(x=10, y=1778).move_to(x=10, y=450).release().perform()
    #     self.go_back()
    #     sleep(2)
    #     self.click(self.locator.show_more)
    #     for _ in range(1, 14):
    #         for i in [2, 14]:
    #             print(i)
    #             # for i in range(2, 15):
    #             try:
    #                 self.click(self.locator.profile_person(i))
    #                 self.click(self.locator.view_profile)
    #                 sleep(1)
    #                 val = self.get_attribute_value(self.data.text_attribute, self.locator.profile_name)
    #                 profile_name.append(val)
    #                 self.driver.swipe(540, 1500, 540, 300, 800)
    #                 val1 = self.get_attribute_value(self.data.content_desc_attribute, self.locator.skype_name)
    #                 print(val, val1)
    #                 skype_name.append(val1.split(',')[-1])
    #                 sleep(1)
    #                 self.go_back()
    #             except WebDriverException:
    #                 self.go_back()
    #         sleep(2)
    #         # self.driver.swipe(540, 1500, 540, 330, 1000)
    #         ele1 = self.driver.find_element_by_xpath(self.locator.profile_person(7))
    #         ele2 = self.driver.find_element_by_xpath(self.locator.profile_person(14))
    #         self.driver.scroll(ele2, ele1)
    #     # sleep(5)
    #     # self.driver.swipe(540, 1500, 540, 350, 800)
    #     # elm = self.find_element(self.locator.profile_person(14))
    #     # action = TouchAction(self.driver)
    #     # action.press(elm).move_to(x=1000, y=2050).release().perform()
    #     #
    #     # TouchAction(self.driver).press(x=1071, y=2074).move_to(x=1071, y=1184).release().perform()
    #     # TouchAction(driver).press(x=1071, y=2077).move_to(x=1062, y=1178).release().perform()

    def extract_group_contact(self):
        sleep(self.data.five_seconds)
        profile_name = []
        skype_name = []
        self.click(self.locator.search)
        self.send_data(self.data.group_name, self.locator.search_input)
        sleep(1)
        self.driver.hide_keyboard()
        self.click(self.locator.select_chat_person(self.data.group_name))
        self.click(self.locator.select_chat_person(self.data.group_name))
        sleep(2)
        # sleep(8)
        # total_members = self.get_attribute_value(self.data.content_desc_attribute, self.locator.total_members)
        # total_members = total_members.split(' ')[0]
        # print(total_members)
        # TouchAction(self.driver).press(x=1077, y=2083).move_to(x=1074, y=1403).release().perform()
        # self.click(self.locator.show_more)
        #

        # actions = TouchAction(self.driver)
        # actions.long_press(None, 1077, 2083)
        # actions.move_to(None, 1074, 1403)
        # actions.perform()

        # self.driver.swipe(540, 1500, 540, 590, 1000)
        # self.driver.swipe(540, 1500, 540, 450, 1000)

        ele1 = self.driver.find_element_by_xpath(self.locator.share_link_to_join)
        ele2 = self.driver.find_element_by_xpath(self.locator.elele)
        self.driver.scroll(ele2, ele1)

        # action = TouchAction(self.driver)
        # # action.press(ele2).move_to(x=10, y=1800).release().perform()
        # # action.press(x=1077, y=2083).move_to(x=1074, y=1403).release().perform()
        # # action.long_press(x=1077, y=2003).move_to(x=1074, y=1403).release().perform()
        # action.long_press(x=10, y=1778).move_to(x=10, y=450).release().perform()
        # self.go_back()
        # sleep(2)
        self.click(self.locator.show_more)
        # val = self.find_elements(self.locator.profile1)
        for _ in range(1, 40):
            elements = self.find_elements(self.locator.profile1)
            for element in elements:
                # try:
                    # self.click(self.locator.profile_person(i))
                    # self.click(self.locator.profile1)
                    print(element)
                    element.click()
                    sleep(3)
                    self.go_back()
                #     self.click(self.locator.view_profile)
                #     sleep(1)
                #     val = self.get_attribute_value(self.data.text_attribute, self.locator.profile_name)
                #     profile_name.append(val)
                #     self.driver.swipe(540, 1500, 540, 300, 800)
                #     val1 = self.get_attribute_value(self.data.content_desc_attribute, self.locator.skype_name)
                #     print(val, val1)
                #     skype_name.append(val1.split(',')[-1])
                #     sleep(1)
                #     self.go_back()
                # except WebDriverException:
                #     self.go_back()
            sleep(3)
            self.driver.swipe(540, 1500, 540, 330, 1000)
            # ele1 = self.driver.find_element_by_xpath(self.locator.profile_person(7))
            # ele2 = self.driver.find_element_by_xpath(self.locator.profile_person(14))
            # self.driver.scroll(ele2, ele1)
        # sleep(5)
        # self.driver.swipe(540, 1500, 540, 350, 800)
        # elm = self.find_element(self.locator.profile_person(14))
        # action = TouchAction(self.driver)
        # action.press(elm).move_to(x=1000, y=2050).release().perform()
        #
        # TouchAction(self.driver).press(x=1071, y=2074).move_to(x=1071, y=1184).release().perform()
        # TouchAction(driver).press(x=1071, y=2077).move_to(x=1062, y=1178).release().perform()
    #
    # def extract_group_contact(self):
    #     sleep(self.data.five_seconds)
    #     profile_name = []
    #     skype_name = []
    #     self.click(self.locator.search)
    #     self.send_data(self.data.group_name, self.locator.search_input)
    #     sleep(1)
    #     self.driver.hide_keyboard()
    #     self.click(self.locator.select_chat_person(self.data.group_name))
    #     self.click(self.locator.select_chat_person(self.data.group_name))
    #     sleep(2)
    #     # total_members = self.get_attribute_value(self.data.content_desc_attribute, self.locator.total_members)
    #     # # total_members = total_members.split(' ')[0]
    #     # print(total_members)
    #     self.scroll_down()
    #     self.scroll_down()
    #     self.scroll_down()

    # element = self.find_element(self.locator.scrollable_element1)
    # vertical_ordinate = 100
    # for i in range(0, 40):
    #     print(vertical_ordinate)
    #     self.driver.execute_script("arguments[0].scrollTop = arguments[1]", element, vertical_ordinate)
    #     sleep(0.2)
    #     # try:
    #     #     val = self.get_text_of_multiple_element(*self.locator.contact_names)
    #     #     contacts.extend(val)
    #     # except Exception as e:
    #     #     pass
    #     #     # print(e)
    #     vertical_ordinate += 400
    #     sleep(0.2)

    # total_members = self.get_attribute_value(self.data.content_desc_attribute, self.locator.total_members)
    # total_members = total_members.split(' ')[0]
    # print(total_members)
    # TouchAction(self.driver).press(x=1077, y=2083).move_to(x=1074, y=1403).release().perform()
    # self.click(self.locator.show_more)
    #

    # actions = TouchAction(self.driver)
    # actions.long_press(None, 1077, 2083)
    # actions.move_to(None, 1074, 1403)
    # actions.perform()

    # self.driver.swipe(540, 1500, 540, 590, 1000)
    # self.driver.swipe(540, 1500, 540, 450, 1000)

    # ele1 = self.driver.find_element_by_xpath(self.locator.share_link_to_join)
    # ele2 = self.driver.find_element_by_xpath(self.locator.elele)
    # # self.driver.scroll(ele2, ele1)
    #
    # action = TouchAction(self.driver)
    # # action.press(ele2).move_to(x=10, y=1800).release().perform()
    # # action.press(x=1077, y=2083).move_to(x=1074, y=1403).release().perform()
    # # action.long_press(x=1077, y=2003).move_to(x=1074, y=1403).release().perform()
    # action.long_press(x=10, y=1778).move_to(x=10, y=450).release().perform()
    # self.go_back()
    # sleep(2)
    # self.click(self.locator.show_more)
    # for _ in range(1, 14):
    #     for i in [2, 14]:
    #         print(i)
    #         # for i in range(2, 15):
    #         try:
    #             self.click(self.locator.profile_person(i))
    #             self.click(self.locator.view_profile)
    #             sleep(1)
    #             val = self.get_attribute_value(self.data.text_attribute, self.locator.profile_name)
    #             profile_name.append(val)
    #             self.driver.swipe(540, 1500, 540, 300, 800)
    #             val1 = self.get_attribute_value(self.data.content_desc_attribute, self.locator.skype_name)
    #             print(val, val1)
    #             skype_name.append(val1.split(',')[-1])
    #             sleep(1)
    #             self.go_back()
    #         except:
    #             self.go_back()
    #     sleep(2)
    #     # self.driver.swipe(540, 1500, 540, 330, 1000)
    #     ele1 = self.driver.find_element_by_xpath(self.locator.profile_person(7))
    #     ele2 = self.driver.find_element_by_xpath(self.locator.profile_person(14))
    #     self.driver.scroll(ele2, ele1)
    #
    # sleep(5)
    # self.driver.swipe(540, 1500, 540, 350, 800)
    # elm = self.find_element(self.locator.profile_person(14))
    # action = TouchAction(self.driver)
    # action.press(elm).move_to(x=1000, y=2050).release().perform()
    #
    # TouchAction(self.driver).press(x=1071, y=2074).move_to(x=1071, y=1184).release().perform()
    # TouchAction(driver).press(x=1071, y=2077).move_to(x=1062, y=1178).release().perform()
