from pages.imo_page import ImoPage
from testcase.imo.base_test_imo import BaseTest


class TestImo(BaseTest):

    def test_whatsapp_02_send_group_message(self):
        introPage = ImoPage(self.driver)
        introPage.send_group_message()

# python3 -m unittest testcase.test_imo_02_send_group_message
