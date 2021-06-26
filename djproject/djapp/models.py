from django.db import models

# Create your models here.
class usermodel(models.Model):
    name = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)