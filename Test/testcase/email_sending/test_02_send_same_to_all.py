# from base_test import BaseTest
from pages.email_page import EmailPage
import unittest


class TestSendAll(unittest.TestCase):

    def test_02_send_email_same_to_all(self):
        email_page = EmailPage()
        email_page.send_same_mail_to_every_one()

