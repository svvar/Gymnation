from django.db import models
from django.core import validators
from .accounts.models import GymUser

# Create your models here.

class Products(models.Model):
    category = models.CharField(max_length=30, null=True)
    picture = models.ImageField(upload_to="productImages")
    name = models.CharField(max_length=100)
    weight = models.IntegerField()
    tastes = models.CharField(max_length=1000, default="Без смаку,Ванільне морозиво,Банан,Полуничний мілкшейк,Шоколад,Кокос")
    price = models.FloatField()
    manufacturer = models.CharField(max_length=50)
    p_type = models.CharField(max_length=50)


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
    photo = models.ImageField(upload_to='trainers', default=None)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
