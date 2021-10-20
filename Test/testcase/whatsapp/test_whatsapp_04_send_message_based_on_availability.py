from pages.whatsapp_page1 import WhatsAppPage
from testcase.whatsapp.base_test_whatsapp import BaseTest


class TestWhatsApp(BaseTest):

    def test_whatsapp_04_send_message_based_on_availability(self):
        intro_page = WhatsAppPage(self.driver)
        intro_page.send_message_based_on_availability()

# python3 -m unittest testcase.test_whatsapp_01_send_message
