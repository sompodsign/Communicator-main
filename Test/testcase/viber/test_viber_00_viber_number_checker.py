from pages.viber_page import ViberPage
from testcase.viber.base_test_viber import BaseTest


class TestWhatsApp(BaseTest):

    def test_viber_00_number_checker(self):
        intro_page = ViberPage(self.driver)
        intro_page.viber_number_finder()
        # intro_page.whatsapp_number_finder_for_escaped_number()

# python3 -m unittest testcase.test_whatsapp_01_send_message
