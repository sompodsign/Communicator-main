from pages.imo_page import ImoPage
from testcase.imo.base_test_imo import BaseTest


class TestImo(BaseTest):

    def test_whatsapp_04_send_message_based_on_availability(self):
        intro_page = ImoPage(self.driver)
        intro_page.send_message_based_on_availability()

# python3 -m unittest testcase.test_imo_01_send_message
