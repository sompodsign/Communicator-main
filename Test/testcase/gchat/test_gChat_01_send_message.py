from pages.gchat_page import GChatPage
from testcase.gchat.base_test_gchat import BaseTest


class TestGChat(BaseTest):

    def test_gChat_01_send_message(self):
        pass
        introPage = GChatPage(self.driver)
        introPage.send_message()


# python3 -m unittest testcase.test_gChat_01_send_message
