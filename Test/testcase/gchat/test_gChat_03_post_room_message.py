from pages.gchat_page import GChatPage
from testcase.gchat.base_test_gchat import BaseTest


class TestGChat(BaseTest):

    def test_gChat_03_post_room_message(self):
        introPage = GChatPage(self.driver)
        introPage.post_room_message()

# python3 -m unittest testcase.test_gChat_03_post_room_message
