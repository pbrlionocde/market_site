from django.contrib.auth.models import User
from django.db import models

from mainapp.constant import DEFAULT_IMAGE, MAX_LEN_NAME

# Create your models here.


class CustomUser(User):
    """Custom registration model"""

    adress = models.TextField(blank=True)


class ItemModel(models.Model):
    """Model for base item"""

    class Meta:
        """Base metaclass"""

        abstract = True

    category = models.CharField(max_length=MAX_LEN_NAME)
    weight = models.FloatField()
    producing_country = models.CharField(max_length=MAX_LEN_NAME)
    manufacturer = models.CharField(max_length=MAX_LEN_NAME)


class Phone(ItemModel):
    model = models.CharField(max_length=MAX_LEN_NAME)
    display = models.FloatField()
    processor = models.CharField(max_length=MAX_LEN_NAME)
    number_cores = models.IntegerField()
    image_url = models.URLField(default=DEFAULT_IMAGE)
