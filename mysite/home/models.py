import email
from typing_extensions import Required
from django.db import models

# Create your models here.
class Index(models.Model):
    name=models.CharField(max_length=122)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    acc=models.CharField(max_length=50)
    ifsc=models.CharField(max_length=50)
    desc=models.TextField(blank=True)
    date=models.DateField()

    def __str__(self):
        return self.name
