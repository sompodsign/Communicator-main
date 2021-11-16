from time import sleep


# from selenium.webdriver.common.action_chains import ActionChains
# from appium.webdriver.common.touch_action import TouchAction
# from appium.webdriver.common.multi_action import MultiAction


class BasePage(object):

    def __init__(self, driver, base_url="about:blank"):
        self.base_url = base_url
        self.driver = driver
        # self.timeout = 30

    def click(self, locator):
        # self.driver.implicitly_wait(1)
        # sleep(1)
        self.driver.find_element_by_xpath(locator).click()

    def click_by_id(self, locator):
        self.driver.find_element_by_id(locator).click()

    def clear_data(self, locator):
        self.driver.find_element_by_xpath(locator).clear()

    def send_data(self, data, locator):
        # self.driver.implicitly_wait(1)
        # sleep(1)
        self.driver.find_element_by_xpath(locator).set_value(data)

    def is_element_displayed(self, locator):
        val = self.driver.find_element_by_xpath(locator).is_displayed()
        return val

    def is_element_displayed_by_id(self, locator):
        val = self.driver.find_element_by_id(locator).is_displayed()
        return val

    def get_attribute_value(self, attributeName, locator):
        val = self.driver.find_element_by_xpath(locator).get_attribute(attributeName)
        return val

    def go_back(self):
        # self.driver.implicitly_wait(1)
        self.driver.back()
        # sleep(1)

    def find_element(self, locator):
        return self.driver.find_element_by_xpath(locator)

    # Search for multiple elements
    def find_elements(self, locator):
        elements = self.driver.find_elements_by_xpath(locator)
        return elements

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def scroll_up(self):
        self.driver.execute_script("window.scrollTo(0,0)")

# size = self.driver.get_window_size()
# print(size)
# x = size['width']
# y = size['height']
# swipe up
# self.driver.swipe(540, 300, 540, 1500, 400)
# swipe down
# self.driver.swipe(540, 1500, 540, 300, 400)


# scrollObject = dict(direction="down", text="some_text", element=appium_driver_elem.id)
# self.driver.execute_script("mobile: scrollTo", scrollObject)

# self.driver.execute_script("mobile: scrollTo", {"element": self.locator.show_more.id})

# TouchAction(self.driver).move_to(self.driver.find_element_by_xpath(self.locator.show_more)).release().perform()
# TouchAction(self.driver).press(x=858, y=1598).move_to(x=858, y=1243).release().perform()

# el = self.driver.find_element_by_id(self.locator.profile_person(14))
# self.driver.execute_script('mobile: scroll', {"element": el, "toVisible": True})


# # Screen width
# width = self.driver.get_window_size()['width']
# # Screen height
# height = self.driver.get_window_size()['height']
#
# self.driver.swipe(width * 0.5, height * 0.9, width * 0.5, height * 0.1, 1000)
# sleep(5)
