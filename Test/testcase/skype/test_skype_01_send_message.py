from pages.skype_page import SkypePage
from testcase.skype.base_test_skype import BaseTest


class TestSkype(BaseTest):

    def test_skype_01_send_message(self):
        introPage = SkypePage(self.driver)
        introPage.send_message()

# python3 -m unittest testcase.test_skype_01_send_message
