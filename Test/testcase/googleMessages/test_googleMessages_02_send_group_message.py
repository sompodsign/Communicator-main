from pages.googleMessages_page import GoogleMessagesPage
from testcase.googleMessages.base_test_googleMessages import BaseTest


class TestGoogleMessages(BaseTest):

    def test_googleMessages_02_send_group_message(self):
        introPage = GoogleMessagesPage(self.driver)
        introPage.test_googleMessages_02_send_group_message()

# python3 -m unittest testcase.test_googleMessages_02_send_group_message
