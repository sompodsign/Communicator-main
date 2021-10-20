from pages.imo_page import ImoPage
from testcase.imo.base_test_imo import BaseTest


class TestImo(BaseTest):

    def test_whatsapp_03_extract_group_contact(self):
        introPage = ImoPage(self.driver)
        introPage.extract_group_contact()

# python3 -m unittest testcase.test_imo_03_extract_group_contact
