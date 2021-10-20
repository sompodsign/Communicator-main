from pages.imo_page import ImoPage
from testcase.imo.base_test_imo import BaseTest


class TestImo(BaseTest):

    def test_whatsapp_04_send_image(self):
        intro_page = ImoPage(self.driver)
        intro_page.send_image()

# python3 -m unittest testcase.test_whatsapp_01_send_message
