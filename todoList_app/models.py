from django.db import models

# Create your models here.

class guest(models.Model):
    task = models.CharField(max_length=255)