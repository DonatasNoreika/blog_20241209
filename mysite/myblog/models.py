from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Pavadinimas", max_length=30)
    content = models.TextField(verbose_name="Tekstas", max_length=4000)
    created = models.DateTimeField(verbose_name="Sukurta", auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']