from django.core import mail
from django.test import TestCase


class EmailTest(TestCase):

    def test_send(self):
        mail.send_mail('subject', 'body.', 'from@example.com', ['to@example.com'])
        assert len(mail.outbox) == 1

    def test_send_again(self):
        mail.send_mail('subject', 'body.', 'from@example.com', ['to@example.com'])
        assert len(mail.outbox) == 1