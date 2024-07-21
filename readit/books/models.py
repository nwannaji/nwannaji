from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=150)
    author = models.ManyToManyField("Authors", related_name="books")
    review = models.TextField(blank=True, null=True)
    review_date = models.DateTimeField(blank=True, null=True)
    is_favorite = models.BooleanField(default=False, verbose_name="Favourite?")

    def __str__(self) -> str:
        return self.title
    
class Authors(models.Model):
    name = models.CharField(max_length=70, help_text="Use pen name, and not real name",
                            unique= True)

    def __str__(self):
        return self.name



