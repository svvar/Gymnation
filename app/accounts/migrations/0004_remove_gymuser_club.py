# Generated by Django 4.2 on 2023-04-16 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_gymuser_club'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gymuser',
            name='club',
        ),
    ]
