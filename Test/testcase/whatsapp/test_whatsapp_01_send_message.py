from pages.whatsapp_page import WhatsAppPage
from testcase.whatsapp.base_test_whatsapp import BaseTest


class TestWhatsApp(BaseTest):

    def test_whatsapp_01_send_message(self):
        intro_page = WhatsAppPage(self.driver)
        intro_page.send_message()

# python3 -m unittest testcase.test_whatsapp_01_send_message
