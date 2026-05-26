from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
import random


def generate_code():
    return str(random.randint(100000, 999999))  # 🔥 string

def exp_time_now():
    return timezone.now() + timedelta(minutes=2)


class VerificationCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)  # 🔥 MUHIM FIX
    expired_date = models.DateTimeField(default=exp_time_now)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = generate_code()
        super().save(*args, **kwargs)

    def is_expired(self):
        return timezone.now() > self.expired_date