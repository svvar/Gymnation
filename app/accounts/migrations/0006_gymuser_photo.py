# Generated by Django 4.2 on 2023-04-16 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_gymuser_club_gymuser_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='gymuser',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='static/dbimages/users'),
        ),
    ]
