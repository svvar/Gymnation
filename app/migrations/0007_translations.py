# Generated by Django 4.2 on 2023-04-08 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_products_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Translations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urlName', models.CharField(max_length=100)),
                ('uaName', models.CharField(max_length=100)),
            ],
        ),
    ]
