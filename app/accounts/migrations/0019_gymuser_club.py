# Generated by Django 4.2 on 2023-04-16 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_gymuser_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='gymuser',
            name='club',
            field=models.CharField(blank=True, choices=[('club1', 'Київ, вул. Уявна 12'), ('club2', 'Київ, вул. Нова 26'), ('club3', 'Київ, вул. Довга 102'), ('club4', 'Київ, вул. Чудова 19'), ('club5', 'Київ, вул. Зелена 66'), ('club6', 'Київ, вул. Технологічна 8')], max_length=100, null=True),
        ),
    ]
