from django.db import models
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from AuthApp.tasks import send_mail_to_user_task
# Create your models here.

@receiver(post_save, sender=User)
def send_mail_to_user(instance,created, **kwargs):
    if created:
        send_mail_to_user_task.delay(instance.email)
        print('ok')




