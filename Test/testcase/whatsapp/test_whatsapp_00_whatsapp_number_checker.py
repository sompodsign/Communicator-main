from pages.whatsapp_page1 import WhatsAppPage
from testcase.whatsapp.base_test_whatsapp import BaseTest


class TestWhatsApp(BaseTest):

    def test_whatsapp_00_number_checker(self):
        intro_page = WhatsAppPage(self.driver)
        # intro_page.whatsapp_number_finder()
        intro_page.collect_available_contacts()

# python3 -m unittest testcase.test_whatsapp_01_send_message
# pytest -s Test/testcase/whatsapp/test_whatsapp_00_whatsapp_number_checker.py