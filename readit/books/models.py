from django.db import models

# Create your models here.
class Books (models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=70, help_text="Use pen name, not real name")
    review = models.TextField(blank=True, null=True)
    review_date = models.DateTimeField(blank=True, null=True)
    is_favorite = models.BooleanField(default=False, verbose_name="Favourite?")

    def __str__(self) -> str:
        return self.title

