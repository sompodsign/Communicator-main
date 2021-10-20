from pages.whatsapp_page import WhatsAppPage
from testcase.whatsapp.base_test_whatsapp import BaseTest


class TestWhatsApp(BaseTest):

    def test_whatsapp_03_extract_group_contact(self):
        introPage = WhatsAppPage(self.driver)
        introPage.extract_group_contact()

# python3 -m unittest testcase.test_whatsapp_03_extract_group_contact
