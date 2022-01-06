from django.db import models
from mainapp.constant import MAX_LEN_NAME
from django.contrib.auth.models import User 

# Create your models here.


class CustomUser(User):
    adress = models.TextField(blank=True)


class ItemModel(models.Model):
    """Model for base item"""

    category = models.CharField(max_length=MAX_LEN_NAME)
    weight = models.FloatField()
    producing_country = models.CharField(max_length=MAX_LEN_NAME)
    manufacturer = models.CharField(max_length=MAX_LEN_NAME)

    class Meta:
        abstract=True


class Phone(ItemModel):
    # manufacturer = models.CharField(max_length=MAX_LEN_NAME)
    model = models.CharField(max_length=MAX_LEN_NAME)
    display = models.FloatField()
    processor = models.CharField(max_length=MAX_LEN_NAME)
    number_cores = models.IntegerField()
    image_url = models.URLField(default='https://beebom.com/wp-content/uploads/2021/09/Download-Android-12.1-Wallpaper-Right-Here.jpg?w=750&quality=75')



