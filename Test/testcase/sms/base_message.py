import unittest
from appium import webdriver
from data.data import Data


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.data = Data
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'platformName': 'Android',
                # 'deviceName': 'emulator-5554',
                'platformVersion': '11',
                'deviceName': '5c26e74d',
                'automationName': 'uiautomator2',
                'newCommandTimeout': '240',
                'appPackage': self.data.messages_app_package,
                'appActivity': self.data.messages_app_home_activity,
                'appWaitPackage': self.data.messages_app_package,
                'appWaitActivity': self.data.messages_app_home_activity,
                'appWaitDuration': '30000',
                'noReset': True,
            })

    def tearDown(self):
        self.driver.quit()
