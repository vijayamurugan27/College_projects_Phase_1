# Generated by Django 4.1.3 on 2022-12-08 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_rename_shirt_size_foods_foodchoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foods',
            name='FoodChoice',
            field=models.CharField(choices=[('Veg', 'Vegetarian'), ('Non-Veg', 'Non-veg'), ('Vegan', 'Vegan')], max_length=10),
        ),
    ]
