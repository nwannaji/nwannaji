from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_artisan = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    location = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=15)

class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

