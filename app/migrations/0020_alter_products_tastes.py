# Generated by Django 4.2 on 2023-05-25 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_alter_products_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='tastes',
            field=models.CharField(default='Без смаку,Ванільне морозиво,Банан,Полуничний мілкшейк,Шоколад,Кокос', max_length=1000),
        ),
    ]
