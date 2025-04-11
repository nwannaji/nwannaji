from django.db import models

from accounts.models import User

# Create your models here.

class ArtisanProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profession = models.CharField(max_length=100)
    experience_years = models.PositiveIntegerField()
    rating = models.FloatField(default=0.0)
    price_range = models.CharField(max_length=50)
    verified = models.BooleanField(default=False)

