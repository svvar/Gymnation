from django.contrib import admin
from .models import Products, GymTrainer
from .accounts.models import GymUser

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "picture"]

admin.site.register(Products, ProductAdmin)
admin.site.register(GymTrainer)
