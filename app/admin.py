from django.contrib import admin
from .models import Products, Translations, Clubs, Plans
from .accounts.models import GymUser

class imageAdmin(admin.ModelAdmin):
    list_display = ["name", "picture"]

class listTranslations(admin.ModelAdmin):
    list_display = ["urlName", "uaName"]

admin.site.register(Products, imageAdmin)
admin.site.register(Translations, listTranslations)
admin.site.register(Clubs)
admin.site.register(Plans)