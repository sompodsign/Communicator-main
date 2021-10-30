# from base_test import BaseTest
from pages.email_page import EmailPage
import unittest


class TestSendEmail(unittest.TestCase):

    def test_01_send_email(self):
        email_page = EmailPage()
        email_page.send_mail()

