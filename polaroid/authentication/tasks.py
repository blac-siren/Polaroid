from __future__ import absolute_import, unicode_literals
import logging
from celery import Task
from django.core.mail import send_mail
from polaroid import celery_app


class Mail(Task):
    ignore_result = True

    def run(self, *args, **kwargs):
        send_mail(
            subject=kwargs.get('subject'),
            message=kwargs.get('message'),
            from_email=kwargs.get('sender'),
            recipient_list=kwargs.get('recipient_list'),
            fail_silently=False)


celery_app.tasks.register(Mail())