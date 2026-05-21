from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


print(" SIGNAL FILE LOADED")


@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):

    if created:
        print(" SIGNAL ISHLADI!")
        print(f"Yangi foydalanuvchi yaratildi: {instance.username}")