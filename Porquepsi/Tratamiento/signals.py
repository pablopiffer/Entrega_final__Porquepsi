from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profesional

@receiver(post_save, sender=User)
def create_user_profesional(sender, instance, created, **kwargs):
    if created:
        Profesional.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profesional(sender, instance, **kwargs):
    instance.profesional.save()

