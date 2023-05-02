from django.db import models
from django.core import validators
from .accounts.models import GymUser

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


# class Translations(models.Model):
#     urlName = models.CharField(max_length=100)
#     uaName = models.CharField(max_length=100)
#
# class Clubs(models.Model):
#     address = models.CharField(max_length=100)
#
# class Plans(models.Model):
#     name = models.CharField(max_length=25)
#     price = models.IntegerField()
#     permissions = models.JSONField()


class Cart(models.Model):
    user = models.ForeignKey(GymUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    taste = models.CharField(max_length=100, default="Без смаку")
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.user}'s cart ({self.id})"

    def total(self):
        return self.price * self.quantity

class GymTrainer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='trainers')

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
