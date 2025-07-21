import smtplib
from twilio.rest import Client

Twilio_Account_SID = "AC5c73a07e65c32ea6da3b23a0602e12f4"
Twilio_Auth_Token = "31958c381a8ce9c914b94918a94f2bb7"
Twilio_Phone_Number = "+15075744375"
my_number = "+390969638363"
smtp_address = "smtp.gmail.com"
email_address = "synelnyk.andrey.1234567890@gmail.com"
email_password = "10293847"

class NotificationManager:

    def __init__(self):
        self.smtp_address = smtp_address
        self.email = email_address
        self.email_password = email_password
        self.twilio_virtual_number = Twilio_Phone_Number
        self.twilio_verified_number = my_number
        self.whatsapp_number = Twilio_Phone_Number
        self.client = Client("AC5c73a07e65c32ea6da3b23a0602e12f4", "31958c381a8ce9c914b94918a94f2bb7")
        self.connection = smtplib.SMTP(smtp_address)

    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_=self.twilio_virtual_number,
            body=message_body,
            to=self.twilio_verified_number
        )
        print(message.sid)

    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:{self.whatsapp_number}',
            body=message_body,
            to=f'whatsapp:{self.twilio_verified_number}'
        )
        print(message.sid)

    def send_emails(self, email_list, email_body):
        with self.connection:
            self.connection.starttls()
            self.connection.login(self.email, self.email_password)
            for email in email_list:
                self.connection.sendmail(
                    from_addr=self.email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode('utf-8')
                )