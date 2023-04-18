from django.db import models
from django.core import validators

# Create your models here.

class Products(models.Model):
    category = models.CharField(max_length=30, null=True)
    picture = models.ImageField(upload_to="static/dbimages")
    name = models.CharField(max_length=100)
    weight = models.IntegerField()
    # tastes = models.CharField(validators=[validators.validate_comma_separated_integer_list], max_length=100)
    tastes = models.JSONField("tastes", default="Без смаку")
    price = models.FloatField()
    manufacturer = models.CharField(max_length=50)
    p_type = models.CharField(max_length=50)


class Translations(models.Model):
    urlName = models.CharField(max_length=100)
    uaName = models.CharField(max_length=100)

class Clubs(models.Model):
    address = models.CharField(max_length=100)

class Plans(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    permissions = models.JSONField()
