from django.core.mail import send_mail

class Mail:

    def __init__(self, subject, message, sender,  recipient_list):
        self.subject = subject
        self.message = message
        self.sender = sender
        self.recipient_list = recipient_list

    @property
    def send_emails(self):
        send_mail(
            subject=self.subject,
            message=self.message,
            from_email=self.sender,
            recipient_list=self.recipient_list,
            fail_silently=False)
