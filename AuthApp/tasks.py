from django.core.mail import send_mail
from celery import shared_task

@shared_task()
def send_mail_to_user_task(email_address):
    send_mail(
            "фидбэк",
            "Thank you!",
            "erbolbaik@mail.ru",
            [email_address],
            fail_silently=False,
        )