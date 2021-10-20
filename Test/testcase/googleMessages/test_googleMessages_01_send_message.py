from pages.googleMessages_page import GoogleMessagesPage
from testcase.googleMessages.base_test_googleMessages import BaseTest


class TestGoogleMessages(BaseTest):

    def test_googleMessages_01_send_message(self):
        introPage = GoogleMessagesPage(self.driver)
        introPage.test_googleMessages_01_send_message()

# python3 -m unittest testcase.test_skype_01_send_message
