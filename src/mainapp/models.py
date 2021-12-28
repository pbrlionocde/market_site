from django.db import models
from django.contrib.auth.models import User 

# Create your models here.


class CustomUser(User):
    adress = models.TextField(blank=True)


class Phone(models.Model):
    manufacturer = models.CharField(max_length=40)
    model = models.CharField(max_length=30)
    display = models.FloatField()
    processor = models.CharField(max_length=30)
    number_cores = models.IntegerField()
