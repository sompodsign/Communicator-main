from pages.skype_page import SkypePage
from testcase.skype.base_test_skype import BaseTest


class TestSkype(BaseTest):

    def test_skype_03_extract_group_contact(self):
        introPage = SkypePage(self.driver)
        introPage.extract_group_contact()

# python3 -m unittest testcase.skype.test_skype_03_extract_group_contact
