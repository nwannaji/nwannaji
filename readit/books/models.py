from django.db import models
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=70, unique=True, help_text="Use pen name, not real name")

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.ManyToManyField(Author, related_name="books")
    review = models.TextField(blank=True, null=True)
    review_date = models.DateTimeField(blank=True, null=True)
    is_favorite = models.BooleanField(default=False, verbose_name="Favorite?")

    def __str__(self):
        return self.title

    def list_authors(self):
        return ", ".join([author.name for author in self.author.all()])

    def save(self, *args, **kwargs):
        if self.review and self.review_date is None:
            self.review_date = timezone.now()  # Corrected assignment operator

        super(Book, self).save(*args, **kwargs)
