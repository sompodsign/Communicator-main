import re
from smtplib import SMTP, SMTP_SSL
import pandas as pd
from data.data import email_file


def validate_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(regex, email):
        return True
    else:
        return False


def read_emails_from_excel(file):
    df = pd.read_excel(file)
    email_series = df["Email"]
    emails = email_series.values.tolist()
    return emails


emails = read_emails_from_excel(email_file)


def write_res_to_excel(file, sheet, data, row):
    df = pd.read_excel(email_file, sheet_name=sheet, header=None)
    df.iloc[row, 1] = data
    df.to_excel(excel_writer=file, sheet_name=sheet, index=False, header=None)


class EmailPage:
    sent_from = 'sooompod@gmail.com'
    subject = 'OMG Super Important Message'
    body = 'Hey, whats up?'

    def send_mail(self):
        """sends dynamic email to addresses one by one and write status in excel sheet"""
        message = f"""\
                Subject: Hi there

                Welcome to QUPS."""
        try:
            server = SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(self.sent_from, '5946644S')
            for i in range(0, len(emails)):
                print(i, emails[i])
                if validate_email(emails[i]):
                    server.sendmail(self.sent_from, emails[i], message)
                    print('Success - {}'.format(emails[i]))
                    write_res_to_excel(email_file, 'Email', 'Success', i + 1)
                else:
                    print("failure - {}".format(emails[i]))
                    write_res_to_excel(email_file, 'Email', 'Invalid', i + 1)
            server.close()
        except Exception as e:
            print("Error {}".format(e))

    def send_same_mail_to_every_one(self):
        """Sends same email to every email addresses in a list"""
        validated_emails = [email for email in emails if validate_email(email)]
        message = f"""\
                Subject: Hi there

                Welcome to QUPS."""
        try:
            server = SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(self.sent_from, '5946644S')
            server.sendmail(self.sent_from, validated_emails, message)
            server.close()
            print("Success")
        except Exception as e:
            print(e)
