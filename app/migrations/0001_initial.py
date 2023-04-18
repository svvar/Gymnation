# Generated by Django 4.2 on 2023-04-06 12:26

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=100)),
                ('weight', models.IntegerField()),
                ('tastes', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')])),
                ('price', models.FloatField()),
                ('manufacturer', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
    ]
