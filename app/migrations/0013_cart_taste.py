# Generated by Django 4.2 on 2023-04-24 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_cart_remove_orderitem_order_remove_orderitem_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='taste',
            field=models.CharField(default='Без смаку', max_length=100),
        ),
    ]
