import unittest
from appium import webdriver
from data.data import Data


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.data = Data
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={'platformName': 'Android',
                                  # 'deviceName': 'emulator-5554',
                                  'platformVersion': '11',
                                  'deviceName': 'c9c5976',
                                  'automationName': 'UiAutomator2',
                                  'newCommandTimeout': '240',
                                  'appPackage': self.data.gchat_app_package,
                                  'appActivity': self.data.gchat_app_activity,
                                  # 'app-package': self.data.gchat_app_package,
                                  # 'app-activity': self.data.gchat_app_activity,
                                  'app': self.data.google_chat,
                                  'appWaitPackage': self.data.gchat_app_package,
                                  'appWaitActivity': self.data.gchat_app_activity,
                                  'appWaitDuration': '30000',
                                  'noReset': True,
                                  'fullReset': False,
                                  # 'autoGrantPermissions': True,
                                  })

    def tearDown(self):
        self.driver.quit()


class TestCase(object):
    pass


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)
    unittest.TextTestRunner(verbosity=1).run(suite)
