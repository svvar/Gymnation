# Generated by Django 4.2 on 2023-04-16 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_gymuser_club_gymuser_plan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gymuser',
            name='club',
            field=models.CharField(blank=True, choices=[('Київ, вул. Уявна 12', 'Київ, вул. Уявна 12'), ('Київ, вул. Нова 26', 'Київ, вул. Нова 26'), ('Київ, вул. Довга 102', 'Київ, вул. Довга 102'), ('Київ, вул. Чудова 19', 'Київ, вул. Чудова 19'), ('Київ, вул. Зелена 66', 'Київ, вул. Зелена 66'), ('Київ, вул. Технологічна 8', 'Київ, вул. Технологічна 8')], max_length=100, null=True),
        ),
    ]