from pages.imo_page import ImoPage
from testcase.imo.base_test_imo import BaseTest


class TestImo(BaseTest):

    def test_whatsapp_01_send_message(self):
        introPage = ImoPage(self.driver)
        introPage.send_message_based_on_availability()

# python3 -m unittest testcase.test_imo_01_send_message
