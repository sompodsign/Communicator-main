

from testcase.sms.base_message import BaseTest
from pages.message import MessagePage


class MessageSend(BaseTest):

    def test_send_messages(self):
        messages_obj = MessagePage(self.driver)
        messages_obj.send_messages()
        # messages_obj.current_activity()
# pytest -s Test/testcase/sms/test_01_send_message.py