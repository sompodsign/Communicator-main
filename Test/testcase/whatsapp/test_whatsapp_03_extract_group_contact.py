from pages.whatsapp_page import WhatsAppPage
from testcase.whatsapp.base_test_whatsapp import BaseTest


class TestWhatsApp(BaseTest):

    def test_whatsapp_03_extract_group_contact(self):
        intro_page = WhatsAppPage(self.driver)
        intro_page.extract_group_contact()

# python3 -m unittest testcase.test_whatsapp_03_extract_group_contact
