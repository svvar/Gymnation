# Generated by Django 4.2 on 2023-04-06 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='type',
            new_name='p_type',
        ),
        migrations.AlterField(
            model_name='products',
            name='picture',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]