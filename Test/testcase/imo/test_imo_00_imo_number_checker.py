from pages.imo_page import ImoPage
from testcase.imo.base_test_imo import BaseTest


class TestImo(BaseTest):

    def test_imo_00_number_checker(self):
        intro_page = ImoPage(self.driver)
        intro_page.imo_number_finder()

# python3 -m unittest testcase.test_imo_01_send_message
