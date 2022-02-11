from tkinter.tix import MAX

from django.db import models

from mainapp.constant import DEFAULT_IMAGE, MAX_DIGITS, MAX_LEN_NAME

# Create your models here.


class ItemModel(models.Model):

    class Meta:
        abstract = True

    category = models.CharField(max_length=MAX_LEN_NAME)
    code_of_product = models.IntegerField()
    price = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=2)
    weight = models.FloatField()
    producing_country = models.CharField(max_length=MAX_LEN_NAME)
    manufacturer = models.CharField(max_length=MAX_LEN_NAME)
    description = models.TextField(max_length=1000)
    dimensions = models.TextField(max_length=400)
    complete_set = models.TextField(max_length=500)



class Phone(ItemModel):
    model = models.CharField(max_length=MAX_LEN_NAME)
    display = models.FloatField()
    processor = models.CharField(max_length=MAX_LEN_NAME)
    number_cores = models.IntegerField()
    image_url = models.URLField(default=DEFAULT_IMAGE)
